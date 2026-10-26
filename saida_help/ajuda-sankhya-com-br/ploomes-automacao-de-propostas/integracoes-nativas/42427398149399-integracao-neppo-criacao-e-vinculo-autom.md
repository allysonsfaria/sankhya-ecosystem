---
id: "42427398149399"
titulo: "Integração Neppo - Criação e vínculo automático de sessões e cards"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427398149399-Integra%C3%A7%C3%A3o-Neppo-Cria%C3%A7%C3%A3o-e-v%C3%ADnculo-autom%C3%A1tico-de-sess%C3%B5es-e-cards"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:15Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12554047", "sync_hash_38f42c3a682f"]
---

# Integração Neppo - Criação e vínculo automático de sessões e cards

## 1. Sobre a criação e vínculo automático de sessões à cards

Ao iniciar uma sessão de atendimento, o sistema cria ou vincula automaticamente um card no funil do Ploomes, agilizando o processo comercial, reduzindo erros e aumentando a produtividade da equipe.

[GIF animado: Imagem 1: Ao iniciar uma sessão de atendimento, o sistema cria ou vincula automaticamente um card no funil do Ploomes, agilizando…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771033645/85f9b60246bef69fe426b12f4cfb/vinculo+automatico.gif?expires=1786536000&signature=a74476eedd11900b493878edea874c922859e2b3229b4d481d84e21f82ec56a5&req=dScgF8l9nodbXPMW3nq%2Bgcf5Ydt15OGFy7HwrC%2FzR%2FmJCfJTy8fx7PhiUutT%0A3aRbdLT5yW9CixzHM7BO7wsHxwQ%3D%0A)

---

## 2. Configurando/Ativando o Vínculo automático de sessões à cards

## 1. Ativação da Funcionalidade

Acesse a área de configuração da integração Neppo no Ploomes e habilite a flag **"Vínculo automático de novas sessões a cards"**. Isso permitirá mapear grupos de atendimento da Neppo aos funis de negócio do Ploomes.

Para acessar a área de configuração da integração acesse: **Administração** > **Integrações** > **Integrações Plug-and-Play** > **Neppo.**

[GIF animado: Imagem 2: Para acessar a área de configuração da integração acesse: Administração > Integrações > Integrações Plug-and-Play >…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771035019/476bd619e439cabf89bb01f66001/acessando+a+integra%C3%A7%C3%A3o+e+ligando+o+vinculo.gif?expires=1786536000&signature=d7df6a225f1f33235dd352fadd3d9fa9736d2000b72b047fca77db92cba9c215&req=dScgF8l9mIFeUPMW3nq%2BgZb%2BzbrWBw2gdop613fX6%2B1I3LGVUNjTa6SHE3Ip%0AkgN8H9suY%2BL70KCMwZDv470HHPQ%3D%0A)

## 2. Mapeamento de Grupos para Funis

Após ativar a funcionalidade, configure o mapeamento:

**Vincule grupos a funis**
Associe cada grupo de atendimento da Neppo a um funil específico do Ploomes.

**Defina o comportamento**
Escolha como os cards serão criados:

- **Sempre criar novo card** – Gera um card a cada sessão
- **Vincular ao último card ou criar novo** – Vincula ao card mais recente do contato no funil configurado ou cria um novo caso não exista

[GIF animado: Imagem 3: Vincular ao último card ou criar novo – Vincula ao card mais recente do contato no funil configurado ou cria um novo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1771036107/11a958692d94066823c53b754c8e/vinculando+grupos.gif?expires=1786536000&signature=3e9ddb1c920e4f325e4101e8ae2890bfb59d644d2804b889ddb378000bef2374&req=dScgF8l9m4BfXvMW3nq%2BgVa4369wqZkvGfdkWSBYNizC1mhOC7lco07wa0B%2B%0AtAjmYJZkZq6pCZsG7pAuYSMQ%2FEc%3D%0A)

⚠️ **Atenção:** Como regra de mapeamento, cada grupo pode ser vinculado a apenas um funil, mas um funil pode receber múltiplos grupos.

---

## 3. Utilizando o Vínculo Automático de Sessões a Cards

## 3.1 Funcionalidade Desabilitada

Com a flag desabilitada, nenhuma ação automática de criação ou vínculo de card será executada. O mapeamento de grupos para funis não ficará disponível.

## 3.2 Comportamento: Sempre Criar Novo Card

A cada nova sessão no grupo configurado, o sistema cria automaticamente um novo card no funil mapeado, independentemente de cards anteriores.

## 3.3 Comportamento: Vincular ao Último Card

O sistema vincula a sessão ao card mais recente do cliente no funil configurado. Se não houver cards anteriores, um novo será criado automaticamente.

## 3.4 Transferência Entre Grupos Durante o Atendimento

Quando um atendimento é transferido para outro grupo:

- O sistema aplica a regra configurada para o novo grupo (criar ou vincular)
- Se ambos os grupos estiverem mapeados para o mesmo funil, nenhuma ação adicional é executada

## 3.5 Registro automático

Toda criação ou vínculo automático de card gera um registro de interação no histórico.

## 3.6 Estrutura do card

- **Cliente:** Empresa (se o contato estiver vinculado a uma) ou o próprio contato
- **Contato do negócio:** Pessoa que iniciou a sessão
- **Nome do card:** Nome do cliente

## 3.7 Cliente Não Cadastrado

Se o cliente não existir no Ploomes:

- Nenhum card será criado automaticamente
- Após criar ou vincular o cliente manualmente, o comportamento configurado será aplicado nas próximas sessões

---

## 4. Limitações e Regras

## 4.1 Funil Indisponível

Se o funil mapeado for excluído ou arquivado, nenhuma ação automática será executada. O sistema criará um registro de interação informando que o funil não está disponível para vínculo.

## 4.2 Regras de Mapeamento

- Cada grupo de atendimento pode ser vinculado a **apenas um funil**
- Um funil pode receber vínculos de **múltiplos grupos** de atendimento

---

## 5. Perguntas Frequentes

## 5.1 O que acontece se o cliente ainda não existe no Ploomes?

Nenhum card será criado até que o cliente seja cadastrado ou vinculado manualmente. Após o cadastro, o comportamento configurado (criar novo ou vincular) será aplicado automaticamente.

## 5.2 Posso mapear vários grupos ao mesmo funil?

Sim. Um funil pode receber múltiplos grupos de atendimento, mas cada grupo só pode ser vinculado a um único funil.

## 5.3 E se o funil for excluído ou arquivado depois?

O sistema criará um registro de interação informando que o funil não está mais disponível e nenhuma ação automática será executada.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
