import { HealthStatus } from "../components/HealthStatus";

export function HomePage() {
  return (
    <section className="panel">
      <h2>Initialisation technique</h2>
      <p>
        La plateforme est prête pour la première phase : dépôt du jeu de données
        et analyse exploratoire. Les tableaux de bord, les prédictions et
        l&apos;assistant ne sont pas encore disponibles.
      </p>
      <HealthStatus />
    </section>
  );
}
