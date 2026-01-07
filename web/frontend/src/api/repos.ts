import type { RepoSummary, RepoDetail, Task, ConfigValue } from "../types";

const API_BASE = "http://localhost:8000/api";

export async function fetchRepos(): Promise<RepoSummary[]> {
  const response = await fetch(`${API_BASE}/repos`);
  if (!response.ok) {
    throw new Error("Failed to fetch repos");
  }
  return response.json();
}

export async function fetchRepo(name: string): Promise<RepoDetail> {
  const response = await fetch(`${API_BASE}/repos/${encodeURIComponent(name)}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch repo: ${name}`);
  }
  return response.json();
}

export async function analyzeRepo(repoUrl: string): Promise<{ task_id: string; status: string }> {
  const response = await fetch(`${API_BASE}/repos`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ repo_url: repoUrl }),
  });
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "Failed to start analysis");
  }
  return response.json();
}

export async function fetchTasks(): Promise<Task[]> {
  const response = await fetch(`${API_BASE}/tasks`);
  if (!response.ok) {
    throw new Error("Failed to fetch tasks");
  }
  return response.json();
}

export async function fetchTask(taskId: string): Promise<Task> {
  const response = await fetch(`${API_BASE}/tasks/${encodeURIComponent(taskId)}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch task: ${taskId}`);
  }
  return response.json();
}

export async function cancelTask(taskId: string): Promise<{ task_id: string; status: string }> {
  const response = await fetch(`${API_BASE}/tasks/${encodeURIComponent(taskId)}`, {
    method: "DELETE",
  });
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "Failed to cancel task");
  }
  return response.json();
}

export async function fetchConfig(): Promise<ConfigValue[]> {
  const response = await fetch(`${API_BASE}/config`);
  if (!response.ok) {
    throw new Error("Failed to fetch config");
  }
  return response.json();
}
