import { useEffect, useState } from "react";
import { FolderGit2, FileCode, Code2, Boxes, ExternalLink, Loader2, ArrowRight, RefreshCw } from "lucide-react";
import { Card, CardContent } from "./ui/card";
import { Badge } from "./ui/badge";
import { Button } from "./ui/button";
import { Skeleton } from "./ui/skeleton";
import { fetchRepos } from "../api/repos";
import type { RepoSummary } from "../types";

interface RepoListProps {
  onSelectRepo: (name: string) => void;
  refreshTrigger?: number;
}

export function RepoList({ onSelectRepo, refreshTrigger }: RepoListProps) {
  const [repos, setRepos] = useState<RepoSummary[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadRepos();
  }, [refreshTrigger]);

  const loadRepos = async () => {
    try {
      setIsLoading(true);
      setError(null);
      const data = await fetchRepos();
      setRepos(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load repositories");
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return (
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <h2 className="text-2xl font-bold">Your Repositories</h2>
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          {[1, 2, 3, 4].map((i) => (
            <Card key={i} className="overflow-hidden">
              <CardContent className="p-6">
                <Skeleton className="h-6 w-32 mb-4" />
                <Skeleton className="h-4 w-48 mb-6" />
                <div className="flex gap-8">
                  <Skeleton className="h-12 w-16" />
                  <Skeleton className="h-12 w-16" />
                  <Skeleton className="h-12 w-16" />
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="space-y-6">
        <h2 className="text-2xl font-bold">Your Repositories</h2>
        <Card className="border-destructive/50 bg-destructive/5">
          <CardContent className="pt-6 text-center">
            <p className="text-destructive mb-4">{error}</p>
            <Button variant="outline" onClick={loadRepos} className="gap-2">
              <RefreshCw className="h-4 w-4" />
              Retry
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  if (repos.length === 0) {
    return (
      <div className="space-y-6">
        <h2 className="text-2xl font-bold">Your Repositories</h2>
        <Card className="border-dashed border-2">
          <CardContent className="py-16 text-center">
            <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-muted mb-4">
              <FolderGit2 className="h-8 w-8 text-muted-foreground" />
            </div>
            <h3 className="text-lg font-medium mb-2">No repositories yet</h3>
            <p className="text-muted-foreground max-w-sm mx-auto">
              Use the form above to analyze your first repository and generate beautiful documentation.
            </p>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold">Your Repositories</h2>
          <p className="text-muted-foreground text-sm mt-1">
            {repos.length} {repos.length === 1 ? "project" : "projects"} documented
          </p>
        </div>
        <Button variant="ghost" size="sm" onClick={loadRepos} className="gap-2">
          <RefreshCw className="h-4 w-4" />
          Refresh
        </Button>
      </div>
      
      <div className="grid gap-4 md:grid-cols-2">
        {repos.map((repo, index) => (
          <Card
            key={repo.name}
            className="group cursor-pointer card-hover overflow-hidden animate-slide-up"
            style={{ animationDelay: `${index * 50}ms` }}
            onClick={() => onSelectRepo(repo.name)}
          >
            <CardContent className="p-0">
              {/* Header */}
              <div className="p-5 pb-4">
                <div className="flex items-start justify-between mb-3">
                  <div className="flex items-center gap-3">
                    <div className="bg-gradient-to-br from-primary/10 to-purple-100 p-2.5 rounded-xl group-hover:from-primary/20 group-hover:to-purple-200 transition-colors">
                      <FolderGit2 className="h-5 w-5 text-primary" />
                    </div>
                    <div>
                      <h3 className="font-semibold text-lg group-hover:text-primary transition-colors">
                        {repo.name}
                      </h3>
                      {repo.has_site && (
                        <span className="inline-flex items-center gap-1 text-xs text-muted-foreground">
                          <ExternalLink className="h-3 w-3" />
                          Docusaurus site
                        </span>
                      )}
                    </div>
                  </div>
                  <StatusBadge status={repo.status} />
                </div>
              </div>
              
              {/* Stats */}
              <div className="px-5 pb-5">
                <div className="flex items-center gap-6 p-4 bg-muted/30 rounded-xl">
                  <StatItem icon={FileCode} value={repo.file_count} label="files" color="text-blue-600" />
                  <div className="w-px h-8 bg-border" />
                  <StatItem icon={Code2} value={repo.function_count} label="functions" color="text-emerald-600" />
                  <div className="w-px h-8 bg-border" />
                  <StatItem icon={Boxes} value={repo.class_count} label="classes" color="text-purple-600" />
                </div>
              </div>
              
              {/* Hover footer */}
              <div className="px-5 pb-4 flex items-center justify-end text-sm text-muted-foreground opacity-0 group-hover:opacity-100 transition-opacity">
                <span className="flex items-center gap-1">
                  View details
                  <ArrowRight className="h-3.5 w-3.5 group-hover:translate-x-0.5 transition-transform" />
                </span>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}

function StatItem({ 
  icon: Icon, 
  value, 
  label, 
  color 
}: { 
  icon: React.ElementType; 
  value: number; 
  label: string;
  color: string;
}) {
  return (
    <div className="flex items-center gap-2.5 flex-1">
      <Icon className={`h-4 w-4 ${color}`} />
      <div>
        <p className="font-semibold text-foreground">{value}</p>
        <p className="text-xs text-muted-foreground">{label}</p>
      </div>
    </div>
  );
}

function StatusBadge({ status }: { status: RepoSummary["status"] }) {
  switch (status) {
    case "complete":
      return (
        <Badge className="bg-emerald-100 text-emerald-700 hover:bg-emerald-100 border-0 gap-1.5">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
          Complete
        </Badge>
      );
    case "in_progress":
      return (
        <Badge variant="secondary" className="gap-1.5 border-0">
          <Loader2 className="h-3 w-3 animate-spin" />
          Processing
        </Badge>
      );
    case "error":
      return (
        <Badge variant="destructive" className="gap-1.5 border-0">
          <span className="w-1.5 h-1.5 rounded-full bg-white" />
          Error
        </Badge>
      );
    default:
      return null;
  }
}
