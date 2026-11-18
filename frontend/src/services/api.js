const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "";

export async function fetchHealth(signal) {
  const response = await fetch(`${API_BASE_URL}/api/health`, { signal });
  if (!response.ok) {
    throw new Error(`Réponse inattendue (${response.status}).`);
  }
  const data = await response.json();
  if (
    data?.status !== "ok" ||
    typeof data.service !== "string" ||
    (data.database !== "up" && data.database !== "down")
  ) {
    throw new Error("La réponse reçue ne correspond pas à l'API de la plateforme.");
  }
  return data;
}
