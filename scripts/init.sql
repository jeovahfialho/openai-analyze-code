CREATE TABLE IF NOT EXISTS analysis_history (
    id SERIAL PRIMARY KEY,
    code_snippet TEXT NOT NULL,
    suggestions JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Índice para buscas por data
CREATE INDEX IF NOT EXISTS idx_analysis_history_created_at 
ON analysis_history(created_at);

-- Função para limpar análises antigas (retenção de 30 dias)
CREATE OR REPLACE FUNCTION cleanup_old_analyses()
RETURNS void AS $$
BEGIN
    DELETE FROM analysis_history
    WHERE created_at < NOW() - INTERVAL '30 days';
END;
$$ LANGUAGE plpgsql;