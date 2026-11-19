import { useQuery } from '@tanstack/react-query';
import { healthService } from '@/services/health';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/Card';
import { Building2, Users, Mail, Send, MessageSquare } from 'lucide-react';

interface StatCardProps {
  title: string;
  value: string;
  description: string;
  icon: React.ReactNode;
  trend?: string;
}

function StatCard({ title, value, description, icon, trend }: StatCardProps) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">{title}</CardTitle>
        <div className="text-muted-foreground">{icon}</div>
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{value}</div>
        <p className="text-xs text-muted-foreground">
          {trend && <span className="text-green-600">{trend}</span>} {description}
        </p>
      </CardContent>
    </Card>
  );
}

export function DashboardPage() {
  const { data: healthData, isLoading } = useQuery({
    queryKey: ['health'],
    queryFn: healthService.checkHealth,
    refetchInterval: 30000, // Refetch every 30 seconds
  });

  if (isLoading) {
    return (
      <div className="flex h-full items-center justify-center">
        <p className="text-muted-foreground">Loading dashboard...</p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Dashboard</h1>
        <p className="text-muted-foreground">
          Welcome to ReachJobAI - Your AI-powered outreach platform
        </p>
      </div>

      {/* System Status */}
      {healthData && (
        <Card className="bg-primary/5 border-primary/20">
          <CardContent className="pt-6">
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-green-500" />
              <p className="text-sm font-medium">
                System Status: <span className="text-primary">{healthData.status}</span>
              </p>
              <span className="text-muted-foreground">•</span>
              <p className="text-sm text-muted-foreground">
                Environment: {healthData.environment}
              </p>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Stats Grid */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-5">
        <StatCard
          title="Companies Discovered"
          value="0"
          description="Ready for outreach"
          icon={<Building2 size={20} />}
        />
        <StatCard
          title="Leads Researched"
          value="0"
          description="Decision makers identified"
          icon={<Users size={20} />}
        />
        <StatCard
          title="Emails Drafted"
          value="0"
          description="AI-generated messages"
          icon={<Mail size={20} />}
        />
        <StatCard
          title="Emails Sent"
          value="0"
          description="Outreach in progress"
          icon={<Send size={20} />}
        />
        <StatCard
          title="Replies Received"
          value="0"
          description="Response rate: 0%"
          icon={<MessageSquare size={20} />}
        />
      </div>

      {/* Recent Activity */}
      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Recent Companies</CardTitle>
            <CardDescription>Recently discovered companies</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex h-32 items-center justify-center text-sm text-muted-foreground">
              No companies discovered yet. Start by discovering new opportunities.
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Active Campaigns</CardTitle>
            <CardDescription>Your ongoing outreach campaigns</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex h-32 items-center justify-center text-sm text-muted-foreground">
              No active campaigns. Create your first campaign to begin outreach.
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Getting Started */}
      <Card>
        <CardHeader>
          <CardTitle>Getting Started</CardTitle>
          <CardDescription>
            Follow these steps to start your job search journey
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="flex items-start gap-4">
              <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary/10 text-sm font-semibold text-primary">
                1
              </div>
              <div>
                <p className="font-medium">Discover Companies</p>
                <p className="text-sm text-muted-foreground">
                  Find relevant companies that match your skills and interests
                </p>
              </div>
            </div>
            <div className="flex items-start gap-4">
              <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary/10 text-sm font-semibold text-primary">
                2
              </div>
              <div>
                <p className="font-medium">Research Decision Makers</p>
                <p className="text-sm text-muted-foreground">
                  Identify and research key decision makers at target companies
                </p>
              </div>
            </div>
            <div className="flex items-start gap-4">
              <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary/10 text-sm font-semibold text-primary">
                3
              </div>
              <div>
                <p className="font-medium">Generate Personalized Emails</p>
                <p className="text-sm text-muted-foreground">
                  Use AI to craft personalized outreach emails based on your profile
                </p>
              </div>
            </div>
            <div className="flex items-start gap-4">
              <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary/10 text-sm font-semibold text-primary">
                4
              </div>
              <div>
                <p className="font-medium">Launch Campaigns</p>
                <p className="text-sm text-muted-foreground">
                  Schedule and manage your outreach campaigns with follow-ups
                </p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
