import { useState } from "react";
import { Rocket, Loader2, Sparkles } from "lucide-react";
import { Button } from "./ui/button";
import { Input } from "./ui/input";
import { Card, CardContent } from "./ui/card";
import { analyzeRepo } from "../api/repos";

interface NewAnalysisFormProps {
  onSuccess: (taskId: string) => void;
}

export function NewAnalysisForm({ onSuccess }: NewAnalysisFormProps) {
  const [repoUrl, setRepoUrl] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!repoUrl.trim()) return;

    setIsLoading(true);
    setError(null);

    try {
      const result = await analyzeRepo(repoUrl.trim());
      setRepoUrl("");
      onSuccess(result.task_id);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to start analysis");
      setIsLoading(false);
    }
  };

  return (
    <Card className="overflow-hidden border-0 shadow-xl shadow-primary/5 bg-gradient-to-br from-white to-purple-50/30">
      <div className="h-1 bg-gradient-to-r from-primary via-purple-500 to-pink-500" />
      <CardContent className="pt-6">
        <div className="flex items-start gap-4 mb-4">
          <div className="bg-gradient-to-br from-primary to-purple-600 p-3 rounded-2xl shadow-lg shadow-primary/25">
            <Rocket className="h-6 w-6 text-white" />
          </div>
          <div>
            <h2 className="text-lg font-semibold flex items-center gap-2">
              Analyze Repository
              <Sparkles className="h-4 w-4 text-amber-500" />
            </h2>
            <p className="text-sm text-muted-foreground">
              Enter a GitHub URL or local path to generate beautiful documentation
            </p>
          </div>
        </div>
        
        <form onSubmit={handleSubmit} className="flex gap-3">
          <Input
            type="text"
            placeholder="https://github.com/user/repo"
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
            disabled={isLoading}
            className="flex-1 h-12 px-4 bg-white border-2 border-muted focus:border-primary/50 rounded-xl transition-colors"
          />
          <Button 
            type="submit" 
            disabled={isLoading || !repoUrl.trim()}
            className="h-12 px-6 rounded-xl bg-gradient-to-r from-primary to-purple-600 hover:from-primary/90 hover:to-purple-600/90 shadow-lg shadow-primary/25 transition-all hover:shadow-xl hover:shadow-primary/30"
          >
            {isLoading ? (
              <>
                <Loader2 className="h-4 w-4 animate-spin" />
                Starting...
              </>
            ) : (
              <>
                <Sparkles className="h-4 w-4" />
                Generate Docs
              </>
            )}
          </Button>
        </form>
        {error && (
          <p className="mt-3 text-sm text-destructive bg-destructive/10 px-3 py-2 rounded-lg">{error}</p>
        )}
      </CardContent>
    </Card>
  );
}
