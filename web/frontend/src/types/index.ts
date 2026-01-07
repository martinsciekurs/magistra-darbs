export interface RepoSummary {
  name: string;
  file_count: number;
  function_count: number;
  class_count: number;
  status: "complete" | "in_progress" | "error";
  has_site: boolean;
}

export interface FunctionDoc {
  node_id: string;
  file: string;
  name: string;
  signature: string;
  docstring: string;
  line_start: number | null;
  line_end: number | null;
}

export interface MethodDoc {
  name: string;
  signature: string;
  docstring: string;
}

export interface ClassDoc {
  class_id: string;
  file: string;
  name: string;
  method_count: number;
  methods: MethodDoc[];
}

export interface RepoDetail {
  name: string;
  files: string[];
  functions: FunctionDoc[];
  classes: ClassDoc[];
}

export interface ProgressStep {
  step: string;
  label: string;
  icon: string;
}

export interface ProgressCount {
  done: number;
  total: number;
}

export interface ProgressDetails {
  files: ProgressCount;
  functions: ProgressCount;
  classes: ProgressCount;
}

export interface TaskProgress {
  completed_steps: string[];
  current_step: ProgressStep;
  progress_percent: number;
  total_steps: number;
  completed_count: number;
  details: ProgressDetails;
}

export interface Task {
  task_id: string;
  repo_url: string;
  status: "queued" | "running" | "complete" | "error" | "cancelled";
  output: string | null;
  error: string | null;
  progress?: TaskProgress;
  started_at?: number;
}

export interface ConfigValue {
  name: string;
  value: string | number | boolean;
  description: string;
}
