---
id: "44011029681943"
titulo: "Integração Salesforce + Meetime Dialer: Como ativar a integração?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011029681943-Integra%C3%A7%C3%A3o-Salesforce-Meetime-Dialer-Como-ativar-a-integra%C3%A7%C3%A3o"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:53:57Z"
rotulos: ["sync_hc", "meetime", "meetime_356", "sync_hash_12ae07873578"]
---

# Integração Salesforce + Meetime Dialer: Como ativar a integração?

## Requisitos para realizar a integração:

- Ser ADMIN na Meetime e no Salesforce
- Ter módulo de API ativada (para conferir vá em Configurações > Busca rápida > Buscar “Perfis (profile)" > Administrador do sistema > Ctrl F: API Ativada).

> Disponível para planos Enterprise, Unlimited, Developer, Performance e Profesisonal com add-on. (Planos Group, Essencials e Professional Edition não possuem API habilitados).

# Salesforce + Módulo Dialer ☎️

### Fluxos da Integração:

Esta integração permite que os usuários realizem ligações diretamente pela Meetime, com os registros sendo sincronizados automaticamente no Salesforce por meio de um botão disponível no objeto configurado dentro do Salesforce.

**Informações enviadas para o histórico do Contato/Deal:**

- Registro da atividade
- Anotações das ligações
- Data, horário e duração da ligação

## Como configurar a integração: Passo a Passo

#### Configurar no Salesforce:

1. **Liberar o atributo type das tarefas:**
   Vá em Configurações > Gerenciador de Objetos > Tarefa > Campos e Relacionamentos > Tipo > 
   Definir Segurança no Nível do Campo. 
   Marque a opção Visível e clique em Salvar.

   [GIF animado: Imagem 1: Liberar o atributo type das tarefas: Vá em Configurações > Gerenciador de Objetos > Tarefa > Campos e Relacionamentos >…](https://ajuda.sankhya.com.br/hc/article_attachments/44011034607511)
2. **Criar tipos de tarefas:**
   Configuração -> Gerenciador de objetos -> Tarefa > Campos e Relacionamentos > Tipo > Criar e insira o seguinte valor:
   • Ligação
   Depois, clique em "Salvar"
   ![Imagem 2: Criar tipos de tarefas: Configuração -> Gerenciador de objetos -> Tarefa > Campos e Relacionamentos > Tipo > Criar e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011030358295)
3. **Liberar CORS:**
   Início > Busca rápida = CORS > Novo > [https://meetime.com.br](https://meetime.com.br/) > salvar

   [GIF animado: Imagem 3: Liberar CORS: Início > Busca rápida = CORS > Novo > https://meetime.com.br > salvar](https://ajuda.sankhya.com.br/hc/article_attachments/44011035251479)

#### Configurar na Meetime:

1. **Integrar na Meetime:**
   Acesse sua conta da Meetime, clique na setinha ao lado do nome do usuário > vá em Integrações > Salesforce > e clique em Integrar.
   ![Imagem 4: Integrar na Meetime: Acesse sua conta da Meetime, clique na setinha ao lado do nome do usuário > vá em Integrações >…](https://ajuda.sankhya.com.br/hc/article_attachments/44011076391063)
2. **Associar atividade:**
   Depois de integrar, relacione os tipos de atividade em “Ir para associação das atividades”. 
   ![Imagem 5: Associar atividade: Depois de integrar, relacione os tipos de atividade em “Ir para associação das atividades”. Associe…](https://ajuda.sankhya.com.br/hc/article_attachments/44011035603735)
   Associe a atividade “Relacionamento” na Meetime com uma atividade no Salesforce. Existe a opção de customização avançada dependendo do resultado da ligação na Meetime — basta clicar em “Avançado” e configurar como desejar.
   ![Imagem 6: Associar atividade: Depois de integrar, relacione os tipos de atividade em “Ir para associação das atividades”. Associe…](https://ajuda.sankhya.com.br/hc/article_attachments/44011035778071)
   ![Imagem 7: Associar atividade: Depois de integrar, relacione os tipos de atividade em “Ir para associação das atividades”. Associe…](https://ajuda.sankhya.com.br/hc/article_attachments/44011077013783)

## Como configurar as ligações integradas: Click-to-call

> A configuração é feita por um usuário ADMIN. Depois disso, os usuários Meetime devem realizar a integração individualmente, acessando Integrações → Salesforce e conectando com a conta correspondente do Salesforce.

1. **Copiar o link Click-to-Call da Meetime:**
   Acesse o painel da Meetime e vá até a área de Integrações. Em seguida, clique em Salesforce e depois em Ver configurações avançadas. Nessa tela, você vai encontrar o link Click-to-Call, é só copiar, ele será utilizado na configuração dentro do Salesforce.

   [GIF animado: Imagem 8: Copiar o link Click-to-Call da Meetime: Acesse o painel da Meetime e vá até a área de Integrações. Em seguida, clique…](https://ajuda.sankhya.com.br/hc/article_attachments/44011031694999)
2. **Criar o botão “Ligar pela Meetime” no Salesforce:**
   No Salesforce, acesse o Gerenciador de Objetos e selecione Oportunidade. Em seguida, vá até Botões, links e ações e clique em Novo botão ou link. No campo de Rótulo, insira o nome “Ligar pela Meetime” e selecione a opção “Botão na página de detalhes”. Depois, cole o link da Meetime no campo de texto grande e salve as alterações.

   [GIF animado: Imagem 9: Criar o botão “Ligar pela Meetime” no Salesforce: No Salesforce, acesse o Gerenciador de Objetos e selecione…](https://ajuda.sankhya.com.br/hc/article_attachments/44011048005271)
3. **Adicionar o botão “Ligar pela Meetime” no layout da Oportunidade:**
   Depois, acesse Layouts de página e selecione o Opportunity Layout (escolha a opção que melhor se encaixa à configuração da sua empresa). Em seguida, vá até Salesforce e Lightning Actions e arraste o botão “Ligar pela Meetime” para a primeira posição, caso sua versão seja Classic, ou para a segunda posição, se estiver utilizando a Lightning. Por fim, salve as alterações.

   [GIF animado: Imagem 10: Adicionar o botão “Ligar pela Meetime” no layout da Oportunidade: Depois, acesse Layouts de página e selecione o…](https://ajuda.sankhya.com.br/hc/article_attachments/44011053482647)
4. **Habilitar campos necessários no Salesforce:**
   Para que a Meetime tenha acesso às informações e números de telefone, é necessário habilitar os seguintes campos nos objetos do Salesforce: 
   **• Contato:** Phone, MobilePhone, OtherPhone e HomePhone 
   **• Lead:** MobilePhone e Phone 
   **• Account:** Phone

> 📌 Observação: Caso algum desses campos não esteja habilitado na sua conta do Salesforce, o recurso de click-to-call da Meetime não funcionará corretamente e será exibida a seguinte mensagem na plataforma:
>
> ![Imagem 11: 📌 Observação: Caso algum desses campos não esteja habilitado na sua conta do Salesforce, o recurso de click-to-call da…](https://ajuda.sankhya.com.br/hc/article_attachments/44011064417943)

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
