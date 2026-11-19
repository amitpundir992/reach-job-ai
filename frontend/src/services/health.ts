import apiClient from '@/lib/api';

export interface HealthResponse {
  status: string;
  app_name: string;
  environment: string;
  api_version?: string;
  database?: string;
}

export const healthService = {
  checkHealth: async (): Promise<HealthResponse> => {
    const response = await apiClient.get<HealthResponse>('/api/v1/health');
    return response.data;
  },

  checkDatabaseHealth: async (): Promise<HealthResponse> => {
    const response = await apiClient.get<HealthResponse>('/api/v1/health/db');
    return response.data;
  },
};
