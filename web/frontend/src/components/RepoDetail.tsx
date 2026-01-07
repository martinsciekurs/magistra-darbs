import { useEffect, useState } from "react";
import { ArrowLeft, FileCode, Code2, Boxes, ChevronRight, Hash, Sparkles } from "lucide-react";
import { Button } from "./ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./ui/tabs";
import { Badge } from "./ui/badge";
import { ScrollArea } from "./ui/scroll-area";
import { Separator } from "./ui/separator";
import { Skeleton } from "./ui/skeleton";
import { fetchRepo } from "../api/repos";
import type { RepoDetail as RepoDetailType, FunctionDoc, ClassDoc } from "../types";

interface RepoDetailProps {
  repoName: string;
  onBack: () => void;
}

export function RepoDetail({ repoName, onBack }: RepoDetailProps) {
  const [repo, setRepo] = useState<RepoDetailType | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadRepo();
  }, [repoName]);

  const loadRepo = async () => {
    try {
      setIsLoading(true);
      setError(null);
      const data = await fetchRepo(repoName);
      setRepo(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load repository");
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return (
      <div className="space-y-6 animate-fade-in">
        <div className="flex items-center gap-4">
          <Button variant="ghost" size="sm" onClick={onBack} className="gap-2">
            <ArrowLeft className="h-4 w-4" />
            Back
          </Button>
          <Skeleton className="h-8 w-48" />
        </div>
        <div className="grid gap-4 grid-cols-3">
          <Skeleton className="h-24" />
          <Skeleton className="h-24" />
          <Skeleton className="h-24" />
        </div>
        <Skeleton className="h-[500px]" />
      </div>
    );
  }

  if (error || !repo) {
    return (
      <div className="space-y-6">
        <Button variant="ghost" size="sm" onClick={onBack} className="gap-2">
          <ArrowLeft className="h-4 w-4" />
          Back
        </Button>
        <Card className="border-destructive/50 bg-destructive/5">
          <CardContent className="pt-6">
            <p className="text-destructive">{error || "Repository not found"}</p>
          </CardContent>
        </Card>
      </div>
    );
  }

  // Group functions by file
  const functionsByFile = repo.functions.reduce((acc, func) => {
    const file = func.file;
    if (!acc[file]) acc[file] = [];
    acc[file].push(func);
    return acc;
  }, {} as Record<string, FunctionDoc[]>);

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header */}
      <div className="flex items-center gap-4">
        <Button variant="ghost" size="sm" onClick={onBack} className="gap-2 hover:bg-primary/5">
          <ArrowLeft className="h-4 w-4" />
          Back
        </Button>
        <div className="flex items-center gap-3">
          <div className="bg-gradient-to-br from-primary/10 to-purple-100 p-2 rounded-xl">
            <Sparkles className="h-5 w-5 text-primary" />
          </div>
          <h1 className="text-2xl font-bold">{repo.name}</h1>
        </div>
      </div>

      {/* Stats */}
      <div className="grid gap-4 grid-cols-3">
        <StatCard
          icon={FileCode}
          value={repo.files.length}
          label="Files"
          color="blue"
        />
        <StatCard
          icon={Code2}
          value={repo.functions.length}
          label="Functions"
          color="emerald"
        />
        <StatCard
          icon={Boxes}
          value={repo.classes.length}
          label="Classes"
          color="purple"
        />
      </div>

      {/* Tabs */}
      <Tabs defaultValue="files" className="w-full">
        <TabsList className="bg-muted/50 p-1">
          <TabsTrigger value="files" className="gap-2 data-[state=active]:bg-white data-[state=active]:shadow-sm">
            <FileCode className="h-4 w-4" />
            Files
          </TabsTrigger>
          <TabsTrigger value="functions" className="gap-2 data-[state=active]:bg-white data-[state=active]:shadow-sm">
            <Code2 className="h-4 w-4" />
            Functions
          </TabsTrigger>
          <TabsTrigger value="classes" className="gap-2 data-[state=active]:bg-white data-[state=active]:shadow-sm">
            <Boxes className="h-4 w-4" />
            Classes
          </TabsTrigger>
        </TabsList>

        {/* Files Tab */}
        <TabsContent value="files" className="mt-4">
          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="text-base font-medium">File Tree</CardTitle>
            </CardHeader>
            <CardContent>
              <ScrollArea className="h-[500px] pr-4">
                <div className="space-y-0.5 font-mono text-sm">
                  {repo.files.map((file, i) => (
                    <div 
                      key={i} 
                      className="flex items-center gap-2 py-2 px-3 rounded-lg hover:bg-muted/50 transition-colors group"
                    >
                      <FileCode className="h-4 w-4 text-blue-500 shrink-0" />
                      <span className="text-muted-foreground group-hover:text-foreground transition-colors">
                        {file}
                      </span>
                    </div>
                  ))}
                </div>
              </ScrollArea>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Functions Tab */}
        <TabsContent value="functions" className="mt-4">
          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="text-base font-medium">Functions by File</CardTitle>
            </CardHeader>
            <CardContent>
              <ScrollArea className="h-[500px] pr-4">
                <div className="space-y-6">
                  {Object.entries(functionsByFile).map(([file, functions]) => (
                    <div key={file} className="animate-slide-up">
                      <div className="flex items-center gap-2 mb-3 sticky top-0 bg-card py-2">
                        <FileCode className="h-4 w-4 text-blue-500" />
                        <span className="font-medium text-sm">{file}</span>
                        <Badge variant="secondary" className="ml-auto text-xs">
                          {functions.length}
                        </Badge>
                      </div>
                      <div className="space-y-2 pl-4 border-l-2 border-muted ml-2">
                        {functions.map((func) => (
                          <FunctionCard key={func.node_id} func={func} />
                        ))}
                      </div>
                      <Separator className="mt-6" />
                    </div>
                  ))}
                </div>
              </ScrollArea>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Classes Tab */}
        <TabsContent value="classes" className="mt-4">
          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="text-base font-medium">Classes</CardTitle>
            </CardHeader>
            <CardContent>
              <ScrollArea className="h-[500px] pr-4">
                <div className="space-y-4">
                  {repo.classes.length === 0 ? (
                    <div className="text-center py-12 text-muted-foreground">
                      <Boxes className="h-12 w-12 mx-auto mb-3 opacity-30" />
                      <p>No classes found in this repository</p>
                    </div>
                  ) : (
                    repo.classes.map((cls, index) => (
                      <ClassCard key={cls.class_id} cls={cls} index={index} />
                    ))
                  )}
                </div>
              </ScrollArea>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}

function StatCard({ 
  icon: Icon, 
  value, 
  label, 
  color 
}: { 
  icon: React.ElementType; 
  value: number; 
  label: string;
  color: "blue" | "emerald" | "purple";
}) {
  const colors = {
    blue: "from-blue-500 to-cyan-500 shadow-blue-500/25",
    emerald: "from-emerald-500 to-teal-500 shadow-emerald-500/25",
    purple: "from-purple-500 to-pink-500 shadow-purple-500/25",
  };
  
  const bgColors = {
    blue: "bg-blue-50",
    emerald: "bg-emerald-50",
    purple: "bg-purple-50",
  };

  return (
    <Card className={`${bgColors[color]} border-0`}>
      <CardContent className="pt-6">
        <div className="flex items-center gap-4">
          <div className={`bg-gradient-to-br ${colors[color]} p-3 rounded-xl shadow-lg`}>
            <Icon className="h-6 w-6 text-white" />
          </div>
          <div>
            <p className="text-3xl font-bold">{value}</p>
            <p className="text-sm text-muted-foreground">{label}</p>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}

function FunctionCard({ func }: { func: FunctionDoc }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="rounded-xl border bg-white p-3 hover:shadow-sm transition-shadow">
      <button
        className="w-full text-left flex items-start gap-2"
        onClick={() => setExpanded(!expanded)}
      >
        <ChevronRight
          className={`h-4 w-4 mt-1 shrink-0 text-muted-foreground transition-transform ${expanded ? "rotate-90" : ""}`}
        />
        <div className="flex-1 min-w-0">
          <p className="font-medium text-sm text-emerald-700">{func.name}</p>
          <p className="text-xs text-muted-foreground font-mono truncate mt-0.5">
            {func.signature}
          </p>
        </div>
        {func.line_start && (
          <Badge variant="outline" className="shrink-0 text-xs gap-1 font-mono">
            <Hash className="h-3 w-3" />
            {func.line_start}
          </Badge>
        )}
      </button>
      {expanded && func.docstring && (
        <div className="mt-3 pt-3 border-t text-sm text-muted-foreground whitespace-pre-wrap pl-6 bg-muted/30 rounded-lg p-3 ml-4">
          {func.docstring}
        </div>
      )}
    </div>
  );
}

function ClassCard({ cls, index }: { cls: ClassDoc; index: number }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <Card 
      className="overflow-hidden animate-slide-up hover:shadow-md transition-shadow"
      style={{ animationDelay: `${index * 30}ms` }}
    >
      <CardHeader className="pb-3 bg-gradient-to-r from-purple-50 to-pink-50">
        <button
          className="w-full text-left flex items-start gap-3"
          onClick={() => setExpanded(!expanded)}
        >
          <ChevronRight
            className={`h-4 w-4 mt-1 shrink-0 text-muted-foreground transition-transform ${expanded ? "rotate-90" : ""}`}
          />
          <div className="flex items-center gap-3 flex-1">
            <div className="bg-gradient-to-br from-purple-500 to-pink-500 p-2 rounded-lg shadow-lg shadow-purple-500/25">
              <Boxes className="h-4 w-4 text-white" />
            </div>
            <div className="flex-1">
              <CardTitle className="text-base font-semibold text-purple-900">
                {cls.name}
              </CardTitle>
              <p className="text-xs text-muted-foreground mt-0.5 font-mono">{cls.file}</p>
            </div>
          </div>
          <Badge className="bg-purple-100 text-purple-700 hover:bg-purple-100 border-0">
            {cls.method_count} methods
          </Badge>
        </button>
      </CardHeader>
      {expanded && cls.methods.length > 0 && (
        <CardContent className="pt-4">
          <div className="space-y-3">
            {cls.methods.map((method, i) => (
              <div key={i} className="text-sm pl-4 border-l-2 border-purple-200">
                <p className="font-medium text-purple-700">{method.name}</p>
                <p className="text-xs text-muted-foreground font-mono truncate">
                  {method.signature}
                </p>
                {method.docstring && (
                  <p className="text-xs text-muted-foreground mt-1 line-clamp-2">
                    {method.docstring}
                  </p>
                )}
              </div>
            ))}
          </div>
        </CardContent>
      )}
    </Card>
  );
}
