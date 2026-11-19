import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  Building2,
  Users,
  Mail,
  Settings,
  TrendingUp,
} from 'lucide-react';
import { cn } from '@/lib/utils';

interface NavItem {
  to: string;
  icon: React.ReactNode;
  label: string;
}

const navItems: NavItem[] = [
  { to: '/', icon: <LayoutDashboard size={20} />, label: 'Dashboard' },
  { to: '/companies', icon: <Building2 size={20} />, label: 'Companies' },
  { to: '/leads', icon: <Users size={20} />, label: 'Leads' },
  { to: '/campaigns', icon: <Mail size={20} />, label: 'Campaigns' },
  { to: '/analytics', icon: <TrendingUp size={20} />, label: 'Analytics' },
  { to: '/settings', icon: <Settings size={20} />, label: 'Settings' },
];

export function Sidebar() {
  return (
    <div className="flex h-full w-64 flex-col border-r bg-card">
      {/* Logo */}
      <div className="flex h-16 items-center border-b px-6">
        <h1 className="text-xl font-bold text-primary">ReachJobAI</h1>
      </div>

      {/* Navigation */}
      <nav className="flex-1 space-y-1 p-4">
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            className={({ isActive }) =>
              cn(
                'flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-colors',
                isActive
                  ? 'bg-primary text-primary-foreground'
                  : 'text-muted-foreground hover:bg-accent hover:text-accent-foreground'
              )
            }
          >
            {item.icon}
            <span>{item.label}</span>
          </NavLink>
        ))}
      </nav>

      {/* Footer */}
      <div className="border-t p-4">
        <p className="text-xs text-muted-foreground">
          © 2024 ReachJobAI
          <br />
          Version 0.1.0
        </p>
      </div>
    </div>
  );
}
