import { useEffect, useState } from "react";
import { Loader2, X, Clock, Zap } from "lucide-react";
import { Card, CardContent } from "./ui/card";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";
import { fetchTasks, cancelTask } from "../api/repos";
import type { Task } from "../types";

interface RunningTasksProps {
  onTaskClick: (taskId: string) => void;
  refreshTrigger?: number;
}

export function RunningTasks({ onTaskClick, refreshTrigger }: RunningTasksProps) {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [cancellingId, setCancellingId] = useState<string | null>(null);

  useEffect(() => {
    loadTasks();
    
    // Poll for updates while there are running tasks
    const pollInterval = setInterval(loadTasks, 2000);
    return () => clearInterval(pollInterval);
  }, [refreshTrigger]);

  const loadTasks = async () => {
    try {
      const data = await fetchTasks();
      // Only show running or queued tasks
      const activeTasks = data.filter(t => t.status === "running" || t.status === "queued");
      setTasks(activeTasks);
    } catch (err) {
      console.error("Failed to load tasks:", err);
    }
  };

  const handleCancel = async (taskId: string, e: React.MouseEvent) => {
    e.stopPropagation();
    setCancellingId(taskId);
    try {
      await cancelTask(taskId);
      loadTasks();
    } catch (err) {
      console.error("Failed to cancel task:", err);
    } finally {
      setCancellingId(null);
    }
  };

  const formatDuration = (startedAt?: number) => {
    if (!startedAt) return "";
    const seconds = Math.floor((Date.now() / 1000) - startedAt);
    if (seconds < 60) return `${seconds}s`;
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}m ${remainingSeconds}s`;
  };

  if (tasks.length === 0) {
    return null;
  }

  return (
    <Card className="border-primary/20 bg-gradient-to-r from-primary/5 to-purple-50/50 overflow-hidden">
      <div className="h-1 bg-gradient-to-r from-primary to-purple-500 animate-pulse" />
      <CardContent className="py-4">
        <div className="flex items-center gap-2 mb-3">
          <Zap className="h-4 w-4 text-primary" />
          <span className="text-sm font-medium">Running Tasks</span>
          <Badge variant="secondary" className="ml-auto">
            {tasks.length} active
          </Badge>
        </div>
        
        <div className="space-y-2">
          {tasks.map((task) => (
            <div
              key={task.task_id}
              className="flex items-center gap-3 p-3 bg-white rounded-xl border shadow-sm cursor-pointer hover:shadow-md transition-shadow"
              onClick={() => onTaskClick(task.task_id)}
            >
              {/* Spinner */}
              <div className="bg-primary/10 p-2 rounded-lg">
                <Loader2 className="h-4 w-4 text-primary animate-spin" />
              </div>
              
              {/* Task info */}
              <div className="flex-1 min-w-0">
                <p className="font-medium text-sm truncate">{task.task_id}</p>
                <div className="flex items-center gap-2 text-xs text-muted-foreground">
                  {task.progress?.current_step && (
                    <span>{task.progress.current_step.label}</span>
                  )}
                  {task.started_at && (
                    <>
                      <span>•</span>
                      <span className="flex items-center gap-1">
                        <Clock className="h-3 w-3" />
                        {formatDuration(task.started_at)}
                      </span>
                    </>
                  )}
                </div>
              </div>
              
              {/* Progress */}
              {task.progress && (
                <Badge variant="outline" className="font-mono text-xs">
                  {task.progress.progress_percent}%
                </Badge>
              )}
              
              {/* Cancel button */}
              <Button
                variant="ghost"
                size="icon-sm"
                className="shrink-0 hover:bg-destructive/10 hover:text-destructive"
                onClick={(e) => handleCancel(task.task_id, e)}
                disabled={cancellingId === task.task_id}
              >
                {cancellingId === task.task_id ? (
                  <Loader2 className="h-4 w-4 animate-spin" />
                ) : (
                  <X className="h-4 w-4" />
                )}
              </Button>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}
