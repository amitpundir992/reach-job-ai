import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';

export function CompaniesPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Companies</h1>
        <p className="text-muted-foreground">
          Discover and manage target companies
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Company Discovery</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex h-64 items-center justify-center text-muted-foreground">
            Company discovery feature coming soon
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
