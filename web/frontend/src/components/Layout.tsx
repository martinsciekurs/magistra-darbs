import { BookOpen, Settings, FolderGit2, Sparkles } from "lucide-react";
import { Button } from "./ui/button";

interface LayoutProps {
  children: React.ReactNode;
  currentPage: "repos" | "settings";
  onNavigate: (page: "repos" | "settings") => void;
}

export function Layout({ children, currentPage, onNavigate }: LayoutProps) {
  return (
    <div className="min-h-screen bg-gradient-subtle">
      {/* Header */}
      <header className="sticky top-0 z-50 border-b border-border/50 bg-white/80 backdrop-blur-md">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            {/* Logo */}
            <div className="flex items-center gap-3">
              <div className="relative">
                <div className="absolute inset-0 bg-primary/20 blur-lg rounded-full" />
                <div className="relative bg-gradient-to-br from-primary to-purple-600 p-2 rounded-xl shadow-lg shadow-primary/25">
                  <BookOpen className="h-5 w-5 text-white" />
                </div>
              </div>
              <div>
                <span className="text-xl font-bold bg-gradient-to-r from-gray-900 to-gray-600 bg-clip-text text-transparent">
                  DocGen
                </span>
                <div className="flex items-center gap-1 text-[10px] text-muted-foreground -mt-0.5">
                  <Sparkles className="h-2.5 w-2.5" />
                  AI-Powered Docs
                </div>
              </div>
            </div>

            {/* Navigation */}
            <nav className="flex items-center gap-1 bg-muted/50 p-1 rounded-xl">
              <Button
                variant={currentPage === "repos" ? "default" : "ghost"}
                size="sm"
                onClick={() => onNavigate("repos")}
                className={`gap-2 rounded-lg ${currentPage === "repos" ? "shadow-md" : ""}`}
              >
                <FolderGit2 className="h-4 w-4" />
                Repositories
              </Button>
              <Button
                variant={currentPage === "settings" ? "default" : "ghost"}
                size="sm"
                onClick={() => onNavigate("settings")}
                className={`gap-2 rounded-lg ${currentPage === "settings" ? "shadow-md" : ""}`}
              >
                <Settings className="h-4 w-4" />
                Settings
              </Button>
            </nav>
          </div>
        </div>
      </header>

      {/* Main content */}
      <main className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 animate-fade-in">
        {children}
      </main>
    </div>
  );
}
