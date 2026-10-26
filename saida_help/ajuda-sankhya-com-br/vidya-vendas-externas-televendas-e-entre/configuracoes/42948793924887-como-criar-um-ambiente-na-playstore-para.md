---
id: "42948793924887"
titulo: "Como Criar um Ambiente na PlayStore para Clientes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948793924887-Como-Criar-um-Ambiente-na-PlayStore-para-Clientes"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T16:50:56Z"
rotulos: ["sync_hc", "vidya", "sync_hash_d30228d4b350", "vidya_528997"]
---

# Como Criar um Ambiente na PlayStore para Clientes

##

Disponibilizar versões de aplicativos na Google Play Store de forma controlada é essencial para garantir testes seguros e entregas planejadas para os clientes. Abaixo, descrevemos o passo a passo de como criar um ambiente de teste fechado na Play Store.

### 1. Acessando o Console da Play Store

Primeiramente, acesse o Google Play Console (<https://play.google.com/console>). Certifique-se de estar logado com uma conta com permissões de gerenciamento de aplicativos.

### 2. Entendendo os Ambientes

Na plataforma, normalmente se trabalha com dois tipos de ambientes:
![Imagem 1: Na plataforma, normalmente se trabalha com dois tipos de ambientes:](https://ajuda.sankhya.com.br/hc/article_attachments/42957190156823)

- **Ambiente Corporativo (com.conceitoapp)**: Usado por clientes com celulares corporativos com controle de instalação de apps, como o Claro Monitor.
- **Ambiente Padrão (com.vidyaforce)**: Usado para versões tradicionais e testes internos em clientes com acesso liberado à Play Store.

### 3. Criando um Ambiente de Teste Fechado

Para criar uma faixa de teste:
![Imagem 2: Para criar uma faixa de teste:](https://ajuda.sankhya.com.br/hc/article_attachments/42957190369047)

1. No menu lateral, vá em **"Testar e lançar" > "Teste fechado"**.
2. Clique em **“Criar faixa”**.
3. Dê um nome à faixa, como `nomeCliente (Teste)` (exemplo: VulcaFlex (Teste)).
4. Clique em **“Criar faixa”**.

### 4. Criando uma Nova Versão Imagem 3: 4. Criando uma Nova Versão

1. Após criar a faixa, clique em **“Criar nova versão”**.
   ![Imagem 4: Após criar a faixa, clique em “Criar nova versão” .](https://ajuda.sankhya.com.br/hc/article_attachments/42957190828183)
2. Na seção **“Versões”**, clique em **“Adicionar da biblioteca”**.
3. Selecione a versão mais recente enviada pela equipe de desenvolvimento (indústria) e clique em **“Adicionar”**.
4. Opcional: adicione notas da versão (release notes).
5. Clique em **“Próximo”**, revise os alertas (normalmente são apenas informativos) e **salve**.

### 5. Adicionando Testadores

Para permitir que clientes testem a versão:

![Imagem 5: Para permitir que clientes testem a versão:](https://ajuda.sankhya.com.br/hc/article_attachments/42957191030423)

1. Acesse novamente a faixa criada.
2. Vá até a seção **"Testadores"**.
3. Crie uma lista com o nome da faixa (ex: vulcaflex teste).
   ![Imagem 6: Crie uma lista com o nome da faixa (ex: vulcaflex teste ).](https://ajuda.sankhya.com.br/hc/article_attachments/42957221042199)
4. Adicione os e-mails manualmente ou importe por planilha.
5. Salve a lista.

⚠️ **Importante:** Certifique-se de que os e-mails são válidos. E-mails inválidos podem impedir o salvamento da lista como um todo.

### 6. Enviando para Revisão

1. Volte para a **visão geral** da faixa.
2. Clique em **“Enviar mudanças para revisão”**.
3. O processo leva de 30 a 40 minutos. Após isso, o status muda de “Em análise” (ícone de relógio) para “Publicado” (ícone verde).
