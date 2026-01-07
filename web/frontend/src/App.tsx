import { useState } from "react";
import { Layout } from "./components/Layout";
import { NewAnalysisForm } from "./components/NewAnalysisForm";
import { RepoList } from "./components/RepoList";
import { RepoDetail } from "./components/RepoDetail";
import { SettingsPage } from "./components/SettingsPage";
import { ProgressModal } from "./components/ProgressModal";
import { RunningTasks } from "./components/RunningTasks";

type Page = "repos" | "settings";

function App() {
  const [currentPage, setCurrentPage] = useState<Page>("repos");
  const [selectedRepo, setSelectedRepo] = useState<string | null>(null);
  const [refreshTrigger, setRefreshTrigger] = useState(0);
  const [activeTaskId, setActiveTaskId] = useState<string | null>(null);

  const handleAnalysisStarted = (taskId: string) => {
    setActiveTaskId(taskId);
  };

  const handleAnalysisComplete = () => {
    setRefreshTrigger((prev) => prev + 1);
  };

  const handleCloseProgress = () => {
    setActiveTaskId(null);
    setRefreshTrigger((prev) => prev + 1);
  };

  const handleTaskClick = (taskId: string) => {
    setActiveTaskId(taskId);
  };

  const handleSelectRepo = (name: string) => {
    setSelectedRepo(name);
  };

  const handleBackToList = () => {
    setSelectedRepo(null);
  };

  const handleNavigate = (page: Page) => {
    setCurrentPage(page);
    setSelectedRepo(null);
  };

  return (
    <>
      <Layout currentPage={currentPage} onNavigate={handleNavigate}>
        {currentPage === "settings" ? (
          <SettingsPage />
        ) : selectedRepo ? (
          <RepoDetail repoName={selectedRepo} onBack={handleBackToList} />
        ) : (
          <div className="space-y-6">
            <NewAnalysisForm onSuccess={handleAnalysisStarted} />
            <RunningTasks 
              onTaskClick={handleTaskClick}
              refreshTrigger={refreshTrigger}
            />
            <RepoList
              onSelectRepo={handleSelectRepo}
              refreshTrigger={refreshTrigger}
            />
          </div>
        )}
      </Layout>

      {/* Progress Modal */}
      {activeTaskId && (
        <ProgressModal
          taskId={activeTaskId}
          onComplete={handleAnalysisComplete}
          onClose={handleCloseProgress}
        />
      )}
    </>
  );
}

export default App;
