---
id: "44011025091735"
titulo: "Integração Salesforce + Meetime Flow: Como ativar a integração?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011025091735-Integra%C3%A7%C3%A3o-Salesforce-Meetime-Flow-Como-ativar-a-integra%C3%A7%C3%A3o"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:53:23Z"
rotulos: ["sync_hc", "meetime", "sync_hash_2e3e6567492e", "meetime_355"]
---

# Integração Salesforce + Meetime Flow: Como ativar a integração?

### Requisitos para realizar a integração:

- Ser ADMIN na Meetime e no Salesforce
- Ter módulo de API ativada (para conferir vá em Configurações > Busca rápida > Buscar “Perfis (profile)" > Administrador do sistema > Ctrl F: API Ativada).

> Disponível para planos Enterprise, Unlimited, Developer, Performance e Profesisonal com add-on. (Planos Group, Essencials e Professional Edition não possuem API habilitados).

## Salesforce + Módulo Flow 👩🏾‍💻

**Fluxos da Integração:**

A integração entre a Meetime e o Salesforce permite a criação de objetos no Salesforce sempre que um Lead é marcado como ganho na Meetime.

**Durante esse processo, são enviados:**

- O histórico completo das interações realizadas durante a prospecção;
- Os dados atualizados do lead no momento da conversão.

**Objetos que podem ser enviados ao Salesforce:**

- Lead
- Conta / Contato / Negócio

**Informações enviadas no Contato/Oportunidade:**

- Campos padrão e campos personalizados mapeados na configuração da prospecção
- Atividades registradas
- Anotações
- Horário e tempo de duração das ligações

**Correspondência de campos no Salesforce:**

1. Organização = Conta
2. Pessoa = Contato
3. Ligação/ Pesquisa / E-mail/ SocialPoint = Task

### Como configurar a integração: Passo a Passo

#### Configurar no Salesforce:

1. **Liberar o atributo type das tarefas:**
   Vá em Configurações > Gerenciador de Objetos > Tarefa > Campos e Relacionamentos > Tipo > Definir Segurança no Nível do Campo. 
   Marque a opção Visível e clique em Salvar.

   ![Imagem 1: Liberar o atributo type das tarefas: Vá em Configurações > Gerenciador de Objetos > Tarefa > Campos e Relacionamentos >…](https://ajuda.sankhya.com.br/hc/article_attachments/44010996163991)
2. **Criar tipos de tarefas:**
   Configuração -> Gerenciador de objetos -> Tarefa > Campos e Relacionamentos > Tipo > Criar e insira os seguintes valores, um por linha:
   • Social point 
   • Ligação relacionamento 
   • Ligação prospecção 
   • Pesquisa 
   • E-mail
   Depois, clique em "Salvar"

   ![Imagem 2: Criar tipos de tarefas: Configuração -> Gerenciador de objetos -> Tarefa > Campos e Relacionamentos > Tipo > Criar e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011005912599)
3. **Liberar CORS:**
   Início > Busca rápida = CORS > Novo > [https://meetime.com.br](https://meetime.com.br/) > salvar

   ![Imagem 3: Liberar CORS: Início > Busca rápida = CORS > Novo > https://meetime.com.br > salvar](https://ajuda.sankhya.com.br/hc/article_attachments/44011006292631)

#### Configurar na Meetime:

1. **Integrar na Meetime:**
   Acesse sua conta da Meetime, clique na setinha ao lado do nome do usuário > vá em Integrações > Salesforce > e clique em Integrar.

   ![Imagem 4: Integrar na Meetime: Acesse sua conta da Meetime, clique na setinha ao lado do nome do usuário > vá em Integrações >…](https://ajuda.sankhya.com.br/hc/article_attachments/44010990806679)
2. **Associar as atividades:**
   Depois de integrar, relacione os tipos de atividade em **“Ir para associação das atividades”**.

   ![Imagem 5: Associar as atividades: Depois de integrar, relacione os tipos de atividade em “Ir para associação das atividades” .](https://ajuda.sankhya.com.br/hc/article_attachments/44011020615319)
3. **Associar campos:**
   Faça a associação dos campos acessando: **Prospecção → Ajustes → Associação de Campos → Editar**.

   ![Imagem 6: Associar campos: Faça a associação dos campos acessando: Prospecção → Ajustes → Associação de Campos → Editar .](https://ajuda.sankhya.com.br/hc/article_attachments/44011012944023)
4. **Configurar a cadência:**
   Para enviar automaticamente os leads ganhos ao Salesforce, ative a **Configuração de saída** dentro de cada cadência: **Meetime → Prospecção → Cadências → Editar cadência → Enviar leads para: Salesforce**.

   ![Imagem 7: Configurar a cadência: Para enviar automaticamente os leads ganhos ao Salesforce, ative a Configuração de saída dentro…](https://ajuda.sankhya.com.br/hc/article_attachments/44011041760407)

#### Configurar Webhook (Opcional):

Essa configuração não gera nenhuma informação visível na tela da Meetime. Isso acontece porque ela serve apenas para que o Salesforce avise a Meetime quando uma oportunidade for marcada como ganha ou perdida dentro do próprio Salesforce.

**Configuração na Meetime:**

1. **Copiar o link do Webhook na Meetime:**
   Para copiar o link, acesse o painel da Meetime e vá até a área de Integrações. Em seguida, clique em Salesforce e depois em Ver configurações avançadas. Nessa tela, você vai encontrar o link do Webhook, é só copiar, ele será utilizado na configuração dentro do Salesforce.

   ![Imagem 8: Copiar o link do Webhook na Meetime: Para copiar o link, acesse o painel da Meetime e vá até a área de Integrações. Em…](https://ajuda.sankhya.com.br/hc/article_attachments/44011007490455)

**Configuração no Salesforce:**

1. Acesse as Configurações do Salesforce: Clique no ícone de **engrenagem** (⚙️) no canto superior direito e selecione **Configurações**.
2. No campo de busca, pesquise por **Regras de fluxo de trabalho**.
3. Selecione **Nova regra e c**lique em **“Prosseguir com Regras de fluxo de trabalho”** quando o sistema solicitar.

   ![Imagem 9: Selecione Nova regra e c lique em “Prosseguir com Regras de fluxo de trabalho” quando o sistema solicitar.](https://ajuda.sankhya.com.br/hc/article_attachments/44011042380055)
4. Em **Objeto**, selecione **Oportunidade e clique em Avançar**
5. Na etapa de edição da regra, em **Nome da Regra**, insira: **enviar op.meetime**
6. Em **Critérios da regra**, configure:
   **Campo:** `Oportunidade:Fase`
   **Operador:** `Igual a`
   **Valor:** Clique na **lupa de pesquisa** ao lado do campo e selecione: **Closed Won e Closed Lost**
7. Clique em **Salvar e Avançar**.

   ![Imagem 10: Clique em Salvar e Avançar .](https://ajuda.sankhya.com.br/hc/article_attachments/44011027713943)
8. Na etapa de **Especificar ações do fluxo de trabalho**: Em **Ações imediatas do fluxo de trabalho**, clique em **Adicionar Ações**.
9. Selecione **Nova mensagem de saída**.
10. Na tela de configuração:
    **Nome:** `Meetime`
    **URL do ponto final:** Cole a URL do **Webhook** copiado dentro da Meetime
    Em **Campos Disponíveis**, adicione os seguintes campos: 
    `Account`
    `Amount`
    `IsClosed`
    `IsWon`
    `LastModifiedDate`
11. Clique em Salvar
12. Você será direcionado novamente para a pagina da etapa 3: Clique em **Concluído**.
13. Após concluir a criação da mensagem de saída: Localize a regra criada na lista.
14. Clique em **Ativar**.

    ![Imagem 11: Clique em Ativar .](https://ajuda.sankhya.com.br/hc/article_attachments/44011028124183)

### Como configurar as ligações integradas: Click-to-call

> A configuração é feita por um usuário ADMIN. Depois disso, os usuários Meetime devem realizar a integração individualmente, acessando Integrações → Salesforce e conectando com a conta correspondente do Salesforce.

1. **Copiar o link Click-to-Call da Meetime:**
   Acesse o painel da Meetime e vá até a área de Integrações. Em seguida, clique em Salesforce e depois em Ver configurações avançadas. Nessa tela, você vai encontrar o link Click-to-Call, é só copiar, ele será utilizado na configuração dentro do Salesforce.

   ![Imagem 12: Copiar o link Click-to-Call da Meetime: Acesse o painel da Meetime e vá até a área de Integrações. Em seguida, clique…](https://ajuda.sankhya.com.br/hc/article_attachments/44011059581975)
2. **Criar o botão “Ligar pela Meetime” no Salesforce:**
   No Salesforce, acesse o Gerenciador de Objetos e selecione Oportunidade. Em seguida, vá até Botões, links e ações e clique em Novo botão ou link. No campo de Rótulo, insira o nome “Ligar pela Meetime” e selecione a opção “Botão na página de detalhes”. Depois, cole o link da Meetime no campo de texto grande e salve as alterações.

   ![Imagem 13: Criar o botão “Ligar pela Meetime” no Salesforce: No Salesforce, acesse o Gerenciador de Objetos e selecione…](https://ajuda.sankhya.com.br/hc/article_attachments/44011044154007)
3. **Adicionar o botão “Ligar pela Meetime” no layout da Oportunidade:**
   Depois, acesse Layouts de página e selecione o Opportunity Layout (escolha a opção que melhor se encaixa à configuração da sua empresa). Em seguida, vá até Salesforce e Lightning Actions e arraste o botão “Ligar pela Meetime” para a primeira posição, caso sua versão seja Classic, ou para a segunda posição, se estiver utilizando a Lightning. Por fim, salve as alterações.

   ![Imagem 14: Adicionar o botão “Ligar pela Meetime” no layout da Oportunidade: Depois, acesse Layouts de página e selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/44011024164887)
4. **Habilitar campos necessários no Salesforce:**
   Para que a Meetime tenha acesso às informações e números de telefone, é necessário habilitar os seguintes campos nos objetos do Salesforce: 
   **• Contato:** Phone, MobilePhone, OtherPhone e HomePhone 
   **• Lead:** MobilePhone e Phone 
   **• Account:** Phone

> 📌 Observação: Caso algum desses campos não esteja habilitado na sua conta do Salesforce, o recurso de click-to-call da Meetime não funcionará corretamente e será exibida a seguinte mensagem na plataforma:
>
> ![Imagem 15: 📌 Observação: Caso algum desses campos não esteja habilitado na sua conta do Salesforce, o recurso de click-to-call da…](https://ajuda.sankhya.com.br/hc/article_attachments/44011024451479)

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
