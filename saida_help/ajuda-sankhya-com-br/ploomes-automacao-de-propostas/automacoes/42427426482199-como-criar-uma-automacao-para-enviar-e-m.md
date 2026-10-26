---
id: "42427426482199"
titulo: "Como criar uma automação para enviar e-mail quando uma reclamação for registrada?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427426482199-Como-criar-uma-automa%C3%A7%C3%A3o-para-enviar-e-mail-quando-uma-reclama%C3%A7%C3%A3o-for-registrada"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:50Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14992759", "sync_hash_0a29a69e21cc"]
---

# Como criar uma automação para enviar e-mail quando uma reclamação for registrada?

Acompanhar reclamações de clientes com agilidade é essencial para garantir um bom atendimento e evitar impactos negativos no relacionamento. Com as automações do Ploomes, é possível identificar registros de interação marcados como reclamação e notificar automaticamente os responsáveis por e-mail, garantindo uma resposta rápida.

## Configuração

## 1. Criar o marcador de reclamação

Antes de configurar a automação, é necessário criar o marcador que será utilizado para identificar as reclamações.

- Acesse **Registros de interação**

- Clique em **Configurar marcadores**

- Crie um novo marcador com o nome **Reclamação** e defina uma cor (exemplo: vermelho)

- Confirme a criação no botão azul

[GIF animado: Imagem 1: Confirme a criação no botão azul](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355093895/0b90aa5b5e8d00dc134f6d28c98f/vivaldi_yDiTLWx1Fb.gif?expires=1786536000&signature=594bab743dba898237d07f5088bd6dc9aae49d582e29620dc58eeb8a58703d45&req=diMiE8l3nolWXPMW3nq%2BgU4HLKYQh2wrc9FhuGAuIW2OEsQybDxrUp0E0BM0%0A4PgQ%2FVRglKZoqeVnMreJTRgcVVs%3D%0A)

## 2. Criar uma nova automação

- Acesse **Administração > Automações**

- Selecione a entidade **Registro de interação**

- Clique em **Nova automação**

[GIF animado: Imagem 2: Clique em Nova automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355095431/5b7d8f8ca481e448862e4f4b2a47/vivaldi_umCHW5wnrb.gif?expires=1786536000&signature=135d11e1f5f6dd52866f7eca74d0040f0702654b8c3d7990efea88aa685749af&req=diMiE8l3mIVcWPMW3nq%2BgaYMWcBg025XMIgmRkHsuwKylIN0YkMc2Hsvx4LI%0A74oz%2BHz%2FYqQIhJDizhuFPus21Wk%3D%0A)

## 3. Configurar descrição, gatilho e filtro

- No campo **Descrição da automação**, informe um nome que identifique a ação
  Exemplo: Disparar e-mail quando uma nova reclamação for registrada

- Em **Quando a automação deve ser disparada**, selecione:

  - Quando o item for criado

- Em seguida, clique no ícone **+** para adicionar o filtro:

  Filtro
  **Marcadores - igual a - Reclamação**

[GIF animado: Imagem 3: Filtro Marcadores - igual a - Reclamação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355098936/e507a7cbc51408a25eb09c48e1ca/vivaldi_zcpm8zJZmI.gif?expires=1786536000&signature=7c248c707086a8e9d3fee3e0830b6af928bb559d9beba25b149bf3aac7db6124&req=diMiE8l3lYhcX%2FMW3nq%2BgY28VZ%2F8RG92oJ9Y3ErZEfr3GLgd9vhLHjXzMRAq%0A497Kr2JskfCCbSyv5pYq4wRJJCQ%3D%0A)

## 4. Definir a ação

- Em **Ao ser disparada, o que a automação deve fazer?**, selecione:

  - **Enviar e-mail**
  - Configure os campos do e-mail:

    **Remetente**: selecione uma forma de configuração de remetente

    **Usuário caso e-mail falhe**
    Selecione um usuário para ser notificado caso o e-mail não seja enviado

    **Destinatário**: selecione o campo de e-mail desejado
    Exemplo: **Negócio > Responsável > E-mail**
    (ou Cliente, se preferir)

    **Assunto**:
    Exemplo: Nova reclamação registrada

    **Conteúdo**:
    Exemplo: Uma nova reclamação foi registrada no sistema.

    Você também pode inserir informações dinâmicas, como a descrição do registro de interação, utilizando os campos disponíveis.

- Clique em **Salvar**

[GIF animado: Imagem 4: Clique em Salvar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2355114537/d92b88bf8511aaf4589ae04d600e/vivaldi_Bt4LnVznO0.gif?expires=1786536000&signature=2692b31d1921b6a46350366bcb9428af3848cc9b9c72593654cc198460c54305&req=diMiE8h%2FmYRcXvMW3nq%2BgWmfPf1yHv4JaB8YYJzsBdqsX6CthVglNx3fZbyy%0AGW2%2B5Vad7RfgGWrU7ADqVa6BY3M%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
