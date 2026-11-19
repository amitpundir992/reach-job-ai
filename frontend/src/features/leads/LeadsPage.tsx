import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';

export function LeadsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Leads</h1>
        <p className="text-muted-foreground">
          Research and manage decision makers
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Lead Management</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex h-64 items-center justify-center text-muted-foreground">
            Lead research feature coming soon
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
