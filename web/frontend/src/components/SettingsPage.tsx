import { useEffect, useState } from "react";
import { Settings, Check, X, Info, Gauge, ToggleLeft, RefreshCw } from "lucide-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./ui/card";
import { Badge } from "./ui/badge";
import { Skeleton } from "./ui/skeleton";
import { Separator } from "./ui/separator";
import { Button } from "./ui/button";
import { fetchConfig } from "../api/repos";
import type { ConfigValue } from "../types";

export function SettingsPage() {
  const [config, setConfig] = useState<ConfigValue[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadConfig();
  }, []);

  const loadConfig = async () => {
    try {
      setIsLoading(true);
      setError(null);
      const data = await fetchConfig();
      setConfig(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load configuration");
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return (
      <div className="space-y-6 animate-fade-in">
        <div className="flex items-center gap-3">
          <div className="bg-gradient-to-br from-gray-100 to-gray-200 p-3 rounded-2xl">
            <Settings className="h-6 w-6 text-gray-600" />
          </div>
          <div>
            <h1 className="text-2xl font-bold">Settings</h1>
            <p className="text-muted-foreground text-sm">Loading configuration...</p>
          </div>
        </div>
        <div className="space-y-4">
          {[1, 2].map((i) => (
            <Card key={i}>
              <CardHeader>
                <Skeleton className="h-6 w-48" />
                <Skeleton className="h-4 w-72" />
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {[1, 2, 3].map((j) => (
                    <div key={j} className="flex items-center justify-between">
                      <Skeleton className="h-4 w-48" />
                      <Skeleton className="h-6 w-24" />
                    </div>
                  ))}
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
      <div className="space-y-6 animate-fade-in">
        <div className="flex items-center gap-3">
          <div className="bg-gradient-to-br from-gray-100 to-gray-200 p-3 rounded-2xl">
            <Settings className="h-6 w-6 text-gray-600" />
          </div>
          <div>
            <h1 className="text-2xl font-bold">Settings</h1>
          </div>
        </div>
        <Card className="border-destructive/50 bg-destructive/5">
          <CardContent className="pt-6 text-center">
            <p className="text-destructive mb-2">{error}</p>
            <p className="text-sm text-muted-foreground mb-4">
              Make sure the backend server is running at http://localhost:8000
            </p>
            <Button variant="outline" onClick={loadConfig} className="gap-2">
              <RefreshCw className="h-4 w-4" />
              Retry
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  // Group configs by category
  const booleanConfigs = config.filter((c) => typeof c.value === "boolean");
  const numberConfigs = config.filter((c) => typeof c.value === "number");
  const stringConfigs = config.filter((c) => typeof c.value === "string");

  return (
    <div className="space-y-6 animate-fade-in">
      <div className="flex items-center gap-3">
        <div className="bg-gradient-to-br from-gray-600 to-gray-800 p-3 rounded-2xl shadow-lg shadow-gray-500/25">
          <Settings className="h-6 w-6 text-white" />
        </div>
        <div>
          <h1 className="text-2xl font-bold">Settings</h1>
          <p className="text-muted-foreground text-sm">
            Configuration from <code className="bg-muted px-1.5 py-0.5 rounded text-xs">config.py</code>
          </p>
        </div>
      </div>

      {/* Feature Flags */}
      <Card className="overflow-hidden">
        <div className="h-1 bg-gradient-to-r from-emerald-400 to-teal-500" />
        <CardHeader>
          <div className="flex items-center gap-2">
            <ToggleLeft className="h-5 w-5 text-emerald-600" />
            <CardTitle>Feature Flags</CardTitle>
          </div>
          <CardDescription>Toggle features on or off</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-1">
            {booleanConfigs.map((item, index) => (
              <div key={item.name}>
                <div className="flex items-center justify-between py-3 px-3 rounded-lg hover:bg-muted/50 transition-colors">
                  <div className="flex-1">
                    <p className="font-medium font-mono text-sm">{item.name}</p>
                    <p className="text-xs text-muted-foreground mt-0.5">{item.description}</p>
                  </div>
                  {item.value ? (
                    <Badge className="bg-emerald-100 text-emerald-700 hover:bg-emerald-100 border-0 gap-1.5">
                      <Check className="h-3 w-3" />
                      Enabled
                    </Badge>
                  ) : (
                    <Badge variant="secondary" className="gap-1.5 border-0">
                      <X className="h-3 w-3" />
                      Disabled
                    </Badge>
                  )}
                </div>
                {index < booleanConfigs.length - 1 && <Separator />}
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Thresholds & Limits */}
      <Card className="overflow-hidden">
        <div className="h-1 bg-gradient-to-r from-blue-400 to-indigo-500" />
        <CardHeader>
          <div className="flex items-center gap-2">
            <Gauge className="h-5 w-5 text-blue-600" />
            <CardTitle>Thresholds & Limits</CardTitle>
          </div>
          <CardDescription>Numeric configuration values</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-1">
            {numberConfigs.map((item, index) => (
              <div key={item.name}>
                <div className="flex items-center justify-between py-3 px-3 rounded-lg hover:bg-muted/50 transition-colors">
                  <div className="flex-1">
                    <p className="font-medium font-mono text-sm">{item.name}</p>
                    <p className="text-xs text-muted-foreground mt-0.5">{item.description}</p>
                  </div>
                  <Badge variant="outline" className="font-mono bg-blue-50 text-blue-700 border-blue-200">
                    {typeof item.value === "number" && item.value >= 1000
                      ? item.value.toLocaleString()
                      : String(item.value)}
                  </Badge>
                </div>
                {index < numberConfigs.length - 1 && <Separator />}
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* String Settings */}
      {stringConfigs.length > 0 && (
        <Card className="overflow-hidden">
          <div className="h-1 bg-gradient-to-r from-purple-400 to-pink-500" />
          <CardHeader>
            <CardTitle>Other Settings</CardTitle>
            <CardDescription>String configuration values</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-1">
              {stringConfigs.map((item, index) => (
                <div key={item.name}>
                  <div className="flex items-center justify-between py-3 px-3 rounded-lg hover:bg-muted/50 transition-colors">
                    <div className="flex-1">
                      <p className="font-medium font-mono text-sm">{item.name}</p>
                      <p className="text-xs text-muted-foreground mt-0.5">{item.description}</p>
                    </div>
                    <Badge variant="outline" className="font-mono">
                      {String(item.value)}
                    </Badge>
                  </div>
                  {index < stringConfigs.length - 1 && <Separator />}
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Info Box */}
      <Card className="bg-gradient-to-br from-amber-50 to-orange-50 border-amber-200/50">
        <CardContent className="pt-6">
          <div className="flex gap-3">
            <div className="bg-amber-100 p-2 rounded-lg h-fit">
              <Info className="h-4 w-4 text-amber-600" />
            </div>
            <div className="text-sm text-amber-900">
              <p className="font-medium mb-1">Read-only Configuration</p>
              <p className="text-amber-700">
                These settings are loaded from <code className="bg-amber-100 px-1.5 py-0.5 rounded text-xs">config.py</code>.
                To modify them, edit the file directly or set environment variables.
              </p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
