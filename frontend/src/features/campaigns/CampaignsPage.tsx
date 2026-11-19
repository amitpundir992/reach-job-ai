import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';

export function CampaignsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Campaigns</h1>
        <p className="text-muted-foreground">
          Manage your outreach campaigns
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Campaign Management</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex h-64 items-center justify-center text-muted-foreground">
            Campaign management feature coming soon
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
