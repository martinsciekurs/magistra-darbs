import { useEffect, useState } from "react";
import { 
  Download, 
  FolderTree, 
  Code, 
  GitBranch, 
  FunctionSquare, 
  Boxes, 
  Globe,
  CheckCircle,
  Loader2,
  Sparkles,
  X,
  FileCode
} from "lucide-react";
import { Card, CardContent } from "./ui/card";
import { Button } from "./ui/button";
import { fetchTask, cancelTask } from "../api/repos";
import type { Task } from "../types";

interface ProgressModalProps {
  taskId: string;
  onComplete: () => void;
  onClose: () => void;
}

const STEP_ICONS: Record<string, React.ElementType> = {
  "download": Download,
  "folder-tree": FolderTree,
  "code": Code,
  "git-branch": GitBranch,
  "function-square": FunctionSquare,
  "boxes": Boxes,
  "globe": Globe,
  "check-circle": CheckCircle,
};

const ALL_STEPS = [
  { step: "fetching", label: "Fetching repository", icon: "download", countKey: null },
  { step: "analyzing", label: "Analyzing file structure", icon: "folder-tree", countKey: "files" },
  { step: "extracting", label: "Extracting code elements", icon: "code", countKey: null },
  { step: "ordering", label: "Building dependency graph", icon: "git-branch", countKey: null },
  { step: "documenting_functions", label: "Documenting functions", icon: "function-square", countKey: "functions" },
  { step: "documenting_classes", label: "Documenting classes", icon: "boxes", countKey: "classes" },
  { step: "generating_site", label: "Generating site", icon: "globe", countKey: null },
];

export function ProgressModal({ taskId, onComplete, onClose }: ProgressModalProps) {
  const [task, setTask] = useState<Task | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isCancelling, setIsCancelling] = useState(false);

  useEffect(() => {
    const pollInterval = setInterval(async () => {
      try {
        const data = await fetchTask(taskId);
        setTask(data);
        
        if (data.status === "complete") {
          clearInterval(pollInterval);
          setTimeout(() => onComplete(), 1500);
        } else if (data.status === "error") {
          clearInterval(pollInterval);
          setError(data.error || "An error occurred");
        } else if (data.status === "cancelled") {
          clearInterval(pollInterval);
          onClose();
        }
      } catch (err) {
        console.log("Waiting for task to start...");
      }
    }, 1000);

    return () => clearInterval(pollInterval);
  }, [taskId, onComplete, onClose]);

  const handleCancel = async () => {
    setIsCancelling(true);
    try {
      await cancelTask(taskId);
      onClose();
    } catch (err) {
      console.error("Failed to cancel:", err);
      setIsCancelling(false);
    }
  };

  const progress = task?.progress;
  const details = progress?.details;
  const isComplete = task?.status === "complete";
  const isError = task?.status === "error";
  const isRunning = task?.status === "running" || task?.status === "queued";

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* Backdrop */}
      <div 
        className="absolute inset-0 bg-black/50 backdrop-blur-sm animate-fade-in"
        onClick={isComplete || isError ? onClose : undefined}
      />
      
      {/* Modal */}
      <Card className="relative z-10 w-full max-w-md mx-4 shadow-2xl animate-slide-up overflow-hidden">
        {/* Gradient header */}
        <div className="h-2 bg-gradient-to-r from-primary via-purple-500 to-pink-500" />
        
        {/* Close button */}
        {(isComplete || isError) && (
          <button
            onClick={onClose}
            className="absolute top-4 right-4 p-1 rounded-full hover:bg-muted transition-colors"
          >
            <X className="h-4 w-4 text-muted-foreground" />
          </button>
        )}
        
        <CardContent className="pt-8 pb-8">
          {/* Header */}
          <div className="text-center mb-6">
            <div className="inline-flex items-center justify-center mb-4">
              {isComplete ? (
                <div className="relative">
                  <div className="absolute inset-0 bg-emerald-400/30 blur-xl rounded-full animate-pulse" />
                  <div className="relative bg-gradient-to-br from-emerald-400 to-teal-500 p-4 rounded-2xl shadow-lg">
                    <CheckCircle className="h-8 w-8 text-white" />
                  </div>
                </div>
              ) : isError ? (
                <div className="bg-gradient-to-br from-red-400 to-rose-500 p-4 rounded-2xl shadow-lg">
                  <X className="h-8 w-8 text-white" />
                </div>
              ) : (
                <div className="relative">
                  <div className="absolute inset-0 bg-primary/30 blur-xl rounded-full animate-pulse" />
                  <div className="relative bg-gradient-to-br from-primary to-purple-600 p-4 rounded-2xl shadow-lg">
                    <Sparkles className="h-8 w-8 text-white animate-pulse" />
                  </div>
                </div>
              )}
            </div>
            
            <h2 className="text-xl font-bold mb-1">
              {isComplete 
                ? "Documentation Complete!" 
                : isError 
                  ? "Analysis Failed" 
                  : "Generating Documentation"}
            </h2>
            <p className="text-sm text-muted-foreground">
              {isComplete 
                ? `${taskId} is ready to explore`
                : isError
                  ? error
                  : `Analyzing ${taskId}...`}
            </p>
          </div>

          {/* Stats row */}
          {!isError && details && (details.files.total > 0 || details.functions.total > 0) && (
            <div className="flex justify-center gap-6 mb-6 p-3 bg-muted/30 rounded-xl">
              {details.files.total > 0 && (
                <StatBadge 
                  icon={FileCode} 
                  done={details.files.done} 
                  total={details.files.total} 
                  label="files"
                  color="blue"
                />
              )}
              {details.functions.total > 0 && (
                <StatBadge 
                  icon={FunctionSquare} 
                  done={details.functions.done} 
                  total={details.functions.total} 
                  label="functions"
                  color="emerald"
                />
              )}
              {details.classes.total > 0 && (
                <StatBadge 
                  icon={Boxes} 
                  done={details.classes.done} 
                  total={details.classes.total} 
                  label="classes"
                  color="purple"
                />
              )}
            </div>
          )}

          {/* Progress bar */}
          {!isError && (
            <div className="mb-6">
              <div className="flex items-center justify-between text-xs text-muted-foreground mb-2">
                <span>Progress</span>
                <span className="font-medium">{progress?.progress_percent ?? 0}%</span>
              </div>
              <div className="h-2.5 bg-muted rounded-full overflow-hidden">
                <div 
                  className="h-full bg-gradient-to-r from-primary via-purple-500 to-pink-500 rounded-full transition-all duration-700 ease-out"
                  style={{ width: `${progress?.progress_percent ?? 0}%` }}
                />
              </div>
            </div>
          )}

          {/* Steps */}
          {!isError && (
            <div className="space-y-1.5">
              {ALL_STEPS.map((stepInfo) => {
                const isStepComplete = progress?.completed_steps.includes(stepInfo.step);
                const isCurrent = progress?.current_step?.step === stepInfo.step;
                const Icon = STEP_ICONS[stepInfo.icon] || Code;
                
                // Get count for this step if available
                type DetailKey = "files" | "functions" | "classes";
                const countKey = stepInfo.countKey as DetailKey | null;
                const count = countKey && details ? details[countKey] : null;
                const showCount = isCurrent && count && count.total > 0;
                
                return (
                  <div
                    key={stepInfo.step}
                    className={`flex items-center gap-3 p-2.5 rounded-xl transition-all duration-300 ${
                      isStepComplete 
                        ? "bg-emerald-50 text-emerald-700" 
                        : isCurrent 
                          ? "bg-primary/5 text-primary ring-1 ring-primary/20" 
                          : "text-muted-foreground/40"
                    }`}
                  >
                    <div className={`p-1.5 rounded-lg transition-all ${
                      isStepComplete 
                        ? "bg-emerald-100" 
                        : isCurrent 
                          ? "bg-primary/10" 
                          : "bg-muted/30"
                    }`}>
                      {isCurrent && !isStepComplete ? (
                        <Loader2 className="h-4 w-4 animate-spin" />
                      ) : isStepComplete ? (
                        <CheckCircle className="h-4 w-4" />
                      ) : (
                        <Icon className="h-4 w-4" />
                      )}
                    </div>
                    <span className="text-sm font-medium flex-1">{stepInfo.label}</span>
                    
                    {/* Show count badge for current step */}
                    {showCount && count && (
                      <span className="text-xs font-mono bg-primary/10 px-2 py-0.5 rounded-full">
                        {count.done}/{count.total}
                      </span>
                    )}
                    
                    {/* Show checkmark count for completed steps with counts */}
                    {isStepComplete && count && count.total > 0 && (
                      <span className="text-xs font-mono bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full">
                        ✓ {count.total}
                      </span>
                    )}
                  </div>
                );
              })}
            </div>
          )}

          {/* Action buttons */}
          <div className="mt-6 flex justify-center gap-3">
            {isRunning && (
              <Button 
                variant="outline"
                onClick={handleCancel}
                disabled={isCancelling}
                className="gap-2"
              >
                {isCancelling ? (
                  <>
                    <Loader2 className="h-4 w-4 animate-spin" />
                    Cancelling...
                  </>
                ) : (
                  <>
                    <X className="h-4 w-4" />
                    Cancel
                  </>
                )}
              </Button>
            )}
            {(isComplete || isError) && (
              <Button 
                onClick={onClose}
                className={isComplete 
                  ? "bg-gradient-to-r from-primary to-purple-600 shadow-lg hover:shadow-xl transition-shadow"
                  : ""
                }
              >
                {isComplete ? "View Repository" : "Close"}
              </Button>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

function StatBadge({ 
  icon: Icon, 
  done, 
  total, 
  label,
  color 
}: { 
  icon: React.ElementType; 
  done: number; 
  total: number;
  label: string;
  color: "blue" | "emerald" | "purple";
}) {
  const colors = {
    blue: "text-blue-600",
    emerald: "text-emerald-600", 
    purple: "text-purple-600",
  };
  
  const isComplete = done >= total;
  
  return (
    <div className="flex items-center gap-2">
      <Icon className={`h-4 w-4 ${colors[color]}`} />
      <div className="text-center">
        <div className="text-sm font-bold">
          {isComplete ? (
            <span className="text-emerald-600">{total}</span>
          ) : (
            <>
              <span className={colors[color]}>{done}</span>
              <span className="text-muted-foreground">/{total}</span>
            </>
          )}
        </div>
        <div className="text-[10px] text-muted-foreground">{label}</div>
      </div>
    </div>
  );
}
