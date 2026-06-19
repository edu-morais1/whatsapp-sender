# whatsapp-sender

Projeto Python que lê contatos cadastrados no Supabase e envia mensagens personalizadas via Z-API no WhatsApp.

A mensagem enviada para cada contato é:
> "Olá, `<nome>` tudo bem com você?"

O envio é limitado a até 3 contatos por execução.

---

## Pré-requisitos

- Python 3.11+
- Conta gratuita no [Supabase](https://supabase.com)
- Conta gratuita no [Z-API](https://z-api.io) com instância conectada ao WhatsApp

---

## Setup da tabela no Supabase

No painel do Supabase, acesse **SQL Editor** e execute:

```sql
CREATE TABLE contatos (
  id BIGSERIAL PRIMARY KEY,
  nome TEXT NOT NULL,
  telefone TEXT NOT NULL UNIQUE,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

INSERT INTO contatos (nome, telefone) VALUES
  ('Maria Silva',  '5544999990001'),
  ('João Pedro',   '5544999990002'),
  ('Ana Paula',    '5544999990003');
```

> O telefone deve estar no formato internacional sem `+` (ex: `5544999990001`).

Após criar a tabela, libere o acesso para a `anon key`:

```sql
GRANT SELECT ON public.contatos TO anon;

ALTER TABLE public.contatos ENABLE ROW LEVEL SECURITY;

CREATE POLICY "allow_select" ON public.contatos
  FOR SELECT TO anon USING (true);
```

---

## Variáveis de ambiente

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

| Variável | Obrigatória | Onde encontrar |
|---|---|---|
| `SUPABASE_URL` | ✅ | Supabase → Settings → General → `https://<project-id>.supabase.co` |
| `SUPABASE_KEY` | ✅ | Supabase → Settings → API Keys → Legacy → **anon public** |
| `SUPABASE_TABLE` | ❌ | Nome da tabela (padrão: `contatos`) |
| `ZAPI_INSTANCE_ID` | ✅ | Z-API → Instâncias Web → ID da instância |
| `ZAPI_TOKEN` | ✅ | Z-API → Instâncias Web → Token da instância |
| `ZAPI_CLIENT_TOKEN` | ❌ | Z-API → Segurança → Token de segurança (opcional) |

---

## Como rodar

```bash
# 1. Clone o repositório
git clone https://github.com/edu-morais1/whatsapp-sender.git
cd whatsapp-sender

# 2. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o .env
cp .env.example .env
# edite o .env com suas credenciais reais

# 5. Execute
python main.py
```

---

## Estrutura do projeto

```
whatsapp-sender/
├── main.py              ← ponto de entrada
├── config.py            ← carrega e valida variáveis de ambiente
├── supabase_client.py   ← lê contatos do Supabase
├── zapi_client.py       ← envia mensagens via Z-API
├── requirements.txt     ← dependências com versões fixadas
├── .env.example         ← template de configuração
└── README.md
```
