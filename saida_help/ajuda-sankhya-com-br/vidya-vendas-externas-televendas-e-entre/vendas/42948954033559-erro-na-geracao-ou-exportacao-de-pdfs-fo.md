---
id: "42948954033559"
titulo: "Erro na Geração ou Exportação de PDFs (Force Mobile)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948954033559-Erro-na-Gera%C3%A7%C3%A3o-ou-Exporta%C3%A7%C3%A3o-de-PDFs-Force-Mobile"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:04:02Z"
rotulos: ["sync_hc", "vidya", "vidya_592583", "sync_hash_6654bf06e95b"]
---

# Erro na Geração ou Exportação de PDFs (Force Mobile)

📌 **O que é este erro?**

Este comportamento crítico ocorre quando o vendedor tenta gerar ou exportar um documento em PDF (como a impressão de uma Nota Fiscal ou espelho de pedido) através do aplicativo móvel, mas a operação é interrompida por uma mensagem de falha na requisição, impedindo a emissão do arquivo.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Aplicativo (Force Mobile)** | Pop-up de erro explícito na tela informando falha ou rejeição na requisição do PDF ao tentar acionar o comando de exportação/impressão. |
| **Navegador (Force Web/Call/Sales)** | Na aba Network (Rede) das ferramentas de desenvolvedor (**F12 / Inspecionar**), a linha de requisição correspondente ao serviço de impressão muda de cor (geralmente para vermelho) indicando um código de erro de API. |

⚙️ **Como Investigar e Diagnosticar (Passo a Passo)**

## 1️⃣ Triagem Inicial (Identificar o escopo)

Antes de analisar códigos, confirme três perguntas essenciais com o usuário para mapear o tamanho do problema:

- Qual documento exato você está tentando imprimir?
- O problema ocorre para todos os documentos (relatórios, boletos) ou apenas um específico (DANFE)?
- O erro acontece com todos os usuários da empresa ou é isolado?

## 2️⃣ Captura da Requisição com Ferramentas Técnicas

Para descobrir qual serviço da API está quebrando, intercepte a comunicação do sistema:

- **No Celular (Via Reqable):** Inicie a captura de dados no Reqable, force o erro do PDF no app e localize a linha da requisição. **Importante:** Copie a requisição (Request) inteira e não apenas o retorno (Response) para conseguir replicá-la depois no Postman.
- **No Computador (Via Navegador):** No Force Web, Call ou Sales, aperte **F12**, vá na aba **Network**, gere o PDF e clique na requisição que retornou com erro para inspecionar os detalhes.

## 🕵️‍♂️ Causa Mais Comum: O "Tipo do Usuário" no Sankhya

Na maioria das vezes, o erro é provocado por falta de permissões na tela de **Autorização de API** do Sankhya, intensificado por uma mudança em versões recentes do ERP que dividiu o cadastro de usuários em duas categorias:

> 👤 **Usuário Interface:** Destinado ao acesso visual humano. Permite logar nas telas do ERP e realizar operações manuais no sistema.
>
> 🤖 **Usuário Integração:** Destinado exclusivamente para comunicação de sistemas via API. As requisições de PDF da Vidya exigem que o usuário que realiza a chamada esteja configurado nesta modalidade.

**Atenção no Ajuste:** Mudar o usuário Vidya para "Integração" pode cortar o acesso dele às telas visuais do Sankhya. Avalie com o cliente a melhor alternativa:

- **Opção 1:** Manter o mesmo usuário Vidya como "Integração", se o cliente não precisar dele acessando telas manualmente.
- **Opção 2 (Recomendada):** Criar dois usuários separados no ERP — um do tipo Interface (para uso visual) e outro do tipo Integração (exclusivo para as APIs da Vidya).

🛠️ **Como Corrigir o Problema**

Depois de garantir que a Vidya está utilizando um usuário configurado como **Integração** no ERP, siga o roteiro abaixo no Sankhya:

## Passo 1: Acessar a tela de Segurança

No menu do ERP Sankhya, busque e abra a tela chamada **Autorização de API**.

## Passo 2: Localizar o Serviço Bloqueado

Utilizando o nome técnico do serviço que você descobriu na etapa de captura (via Reqable, Navegador ou Postman), pesquise o item correspondente e abra o cadastro dessa autorização.

## Passo 3: Conceder a Permissão

Inclua o usuário de integração utilizado pela Vidya na lista de usuários autorizados a consumir aquele serviço específico. Salve a alteração.

## Passo 4: Validar em Campo

Peça para o vendedor realizar uma nova sincronização manual no aplicativo, tente gerar o PDF novamente e valide se o documento é emitido normalmente.

💡 **Observações Importantes**

- 🛑 **Bloqueio Administrativo:** Nem todo usuário tem acesso à tela de Autorização de API no ERP. Na esmagadora maioria dos clientes, essa trava só pode ser liberada por usuários administradores master (como o usuário **SUP**). Se você não tiver esse acesso, solicite o apoio direto do responsável pelo TI/Sankhya do cliente.
