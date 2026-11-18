export function AppLayout({ children }) {
  return (
    <div className="app-shell">
      <header className="app-header">
        <p className="eyebrow">PFA — Data Science et Intelligence Artificielle</p>
        <h1>Productivité étudiante</h1>
      </header>
      <main className="app-main">{children}</main>
    </div>
  );
}
