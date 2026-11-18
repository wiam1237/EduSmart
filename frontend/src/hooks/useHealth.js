import { useCallback, useEffect, useState } from "react";

import { fetchHealth } from "../services/api";

export function useHealth() {
  const [requestId, setRequestId] = useState(0);
  const [state, setState] = useState({
    status: "loading",
    data: null,
    error: null,
  });

  const refresh = useCallback(() => {
    setState((current) => ({ ...current, status: "loading", error: null }));
    setRequestId((value) => value + 1);
  }, []);

  useEffect(() => {
    const controller = new AbortController();

    fetchHealth(controller.signal)
      .then((data) => {
        setState({ status: "ready", data, error: null });
      })
      .catch((error) => {
        if (error.name === "AbortError") {
          return;
        }
        setState({
          status: "error",
          data: null,
          error: "L'API est injoignable. Démarrez le backend, puis réessayez.",
        });
      });

    return () => controller.abort();
  }, [requestId]);

  return { ...state, refresh };
}
