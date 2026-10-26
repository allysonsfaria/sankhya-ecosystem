---
id: "39378066483351"
titulo: "Tela \"Gestão de Licenças\" não aparece mesmo após liberação de acesso"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39378066483351-Tela-Gest%C3%A3o-de-Licen%C3%A7as-n%C3%A3o-aparece-mesmo-ap%C3%B3s-libera%C3%A7%C3%A3o-de-acesso"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-19T19:32:56Z"
rotulos: ["Produtos", "Configuração", "Atualização", "Preferências", "Erro", "Artigo criado KCS", "Plataforma - KCS"]
---

# Tela "Gestão de Licenças" não aparece mesmo após liberação de acesso

**MENSAGEM**

A tela "Gestão de Licenças" não é exibida, mesmo com a liberação de acesso concedida ao usuário.

**SITUAÇÃO**

O usuário tenta acessar o caminho **Configurações > Avançado > Gestão de Licenças**, mas a tela não consta no menu. Isso impede o gerenciamento de acessos e a liberação de licenças travadas.

**SOLUÇÃO**

Para resolver este problema, siga os passos abaixo:

**(1)** **Verifique o Parâmetro:**

Acesse **Configurações > Avançado > Preferências** e busque por `INITSASONLINE`.

- Caso não exista, crie-o manualmente: \* **Chave:** `INITSASONLINE` | **Tipo:** Lógico | **Valor:** Ligado.
- M**ódulo/Menu/Aba:** Configurações / Diversas / Diversas.

**(2)** **Reinicie o parâmetro**

- Desligue o parâmetro `INITSASONLINE` e **Salve**.
- Ligue o parâmetro novamente e **Salve**.

**(3)** **Validação**

- Peça ao usuário afetado para atualizar o sistema (F5) ou realizar um novo login.
- Verifique se a tela **Gestão de Licenças** passou a ser exibida no caminho: **Configurações > Avançado > Gestão de Licenças**.

**CAUSA**

A ausência da tela ocorre devido à falta de inicialização do serviço SAS Online no ambiente. O parâmetro `INITSASONLINE` força a ativação dessa interface moderna de gestão.
