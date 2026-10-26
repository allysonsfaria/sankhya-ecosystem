---
id: "33721270326167"
titulo: "Erro: Falha ao carregar metadados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33721270326167-Erro-Falha-ao-carregar-metadados"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:28:24Z"
rotulos: ["Configuração", "Erro", "Falha validação licença", "cache", "Erro: Falha ao carregar metadados", "metadados", "Sankhya"]
---

# Erro: Falha ao carregar metadados

MENSAGEM

Erro: Falha ao carregar metadados.

SITUAÇÃO

Ao acessar qualquer tela ou função no sistema Sankhya, como **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas), **"Portal de Compras"** (Comercial » Consulta » Portal de Compras) ou **"Consulta de Produtos"** (Pedido Web » Consulta de Produtos), o sistema apresenta a mensagem de erro. Ocorre **apenas em uma máquina específica**, enquanto em outros computadores o acesso permanece normal.

Para identificar se o problema é local:

**(1)**  Verifique se o erro ocorre em outros navegadores (ex.: Google Chrome, Edge) ou em outros computadores. 

**(2)**  Se ocorrer **somente em uma máquina**, é um indicativo de problema local de cache.

SOLUÇÃO

Siga o passo a passo para resolver o problema:

**(1)**  **Limpe o cache do navegador:**

- Feche todas as abas dentro do **"Navegador Sankhya"**.
- Limpe cache e cookies do navegador.
- Aguarde alguns segundos e abra novamente o sistema.

**(1)**  **Passo a passo detalhado:** 

![Imagem 1: (1) Passo a passo detalhado:](https://ajuda.sankhya.com.br/hc/article_attachments/34101255923479) 

- Após fechar as abas dentro do **"Navegador Sankhya"**, na parte superior da tela clique nos **3 pontos na vertical**.

![Imagem 2: Após fechar as abas dentro do "Navegador Sankhya" , na parte superior da tela clique nos 3 pontos na vertical .](https://ajuda.sankhya.com.br/hc/article_attachments/34101255925527) 

- Clique em **"LIMPAR CACHE"**.

![Imagem 3: Clique em "LIMPAR CACHE" .](https://ajuda.sankhya.com.br/hc/article_attachments/34101269849879) 

- Clique em **"SIM"** para concluir a limpeza do cache.

Após a limpeza, o navegador irá fechar e voltar ao menu principal de login. Teste o acesso novamente nas abas que estavam com o problema. 

**(2)**  **Se o problema persistir:**

- Agende a reinicialização do sistema **fora do horário de expediente** para não impactar a operação.
- Reinicie o sistema em **"Administração"** > **"Reinicializar Sistema do Sankhya",** se necessário com orientação de um consultor de suporte ou time de TI interno, **pois essa reinicialização derruba a base de produção.**

CAUSA

O erro ocorre devido ao **cache local cheio ou corrompido no navegador**, impedindo o carregamento dos metadados necessários para renderizar a tela corretamente.
