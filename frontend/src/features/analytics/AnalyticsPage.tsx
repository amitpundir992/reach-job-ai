import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';

export function AnalyticsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Analytics</h1>
        <p className="text-muted-foreground">
          Track your outreach performance
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Performance Analytics</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex h-64 items-center justify-center text-muted-foreground">
            Analytics feature coming soon
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
