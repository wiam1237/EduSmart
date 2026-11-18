import { useHealth } from "../hooks/useHealth";

const DATABASE_LABELS = {
  up: "PostgreSQL répond",
  down: "PostgreSQL est injoignable",
};

export function HealthStatus() {
  const { status, data, error, refresh } = useHealth();

  return (
    <div className="health" aria-live="polite">
      <h3>État de l&apos;API</h3>
      {status === "loading" && <p>Vérification en cours…</p>}
      {status === "error" && <p className="health-error">{error}</p>}
      {status === "ready" && data && (
        <dl>
          <div>
            <dt>Service</dt>
            <dd>{data.service}</dd>
          </div>
          <div>
            <dt>API</dt>
            <dd>{data.status}</dd>
          </div>
          <div>
            <dt>Base de données</dt>
            <dd>{DATABASE_LABELS[data.database] ?? data.database}</dd>
          </div>
        </dl>
      )}
      <button type="button" onClick={refresh}>
        Vérifier à nouveau
      </button>
    </div>
  );
}
