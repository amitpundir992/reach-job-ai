export interface User {
  id: string;
  email: string;
  full_name?: string;
  created_at: string;
}

export interface ApiError {
  detail: string;
  message?: string;
}
