---
id: "42427405319447"
titulo: "Campo do tipo Desenvolvedor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427405319447-Campo-do-tipo-Desenvolvedor"
trilha: "PLOOMES: Automação de propostas  > FAQ > Campos e formulários"
atualizado_em: "2026-08-03T12:59:07Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12601635", "sync_hash_08bf79fe7c7e"]
---

# Campo do tipo Desenvolvedor

## 1) Sobre o Campo do tipo Desenvolvedor

O **Campo do tipo Desenvolvedor** permite criar componentes personalizados dentro do Ploomes com **HTML, CSS e JavaScript**, ampliando a experiência do CRM para necessidades específicas — por exemplo: exibir dados externos, criar miniaplicações, validar entradas ou promover interações dinâmicas diretamente nos formulários. O código é **sempre renderizado em um iframe**, garantindo isolamento e segurança. Recursos nativos como **PloomesServer** (requisições seguras à API do Ploomes) e **PloomesDocument** (acesso ao `document` da aplicação principal, apenas na Web) dão mais poder ao desenvolvedor para integrar e orquestrar comportamentos com o restante do sistema.

---

## 2) Pré-requisitos

- Ter o **módulo de CPQ** contratado e habilitado na conta.
- Ser **Administrador** do Ploomes (somente administradores editam/configuram este tipo de campo).
- Conhecimento básico de **HTML, CSS e JavaScript**.
- (Recomendado) Familiaridade com **API do Ploomes** e com a classe **PloomesServer**.

---

## 3) Configurando/Ativando o Campo do tipo Desenvolvedor

## 3.1) Abrindo a configuração (modal)

1. Acesse **Configurações → Campos personalizados** e crie um campo do tipo **Desenvolvedor**.
2. Clique em **Configurar campo** para abrir o **modal de configuração**.
3. Na primeira edição, um **código padrão** é carregado automaticamente; você pode **restaurá-lo** a qualquer momento com **Resetar campo**.

## 3.2) Escrevendo e testando o código (HTML, CSS e JS)

- O modal permite editar **HTML**, **CSS** e **JavaScript** do campo.
- O conteúdo salvo é gravado como **valor padrão** do campo e será renderizado no iframe.
- Use **Testar código** para visualizar imediatamente o resultado.

**Importante sobre persistência**: por ser um campo renderizado em iframe, o valor salvo do campo pode **não refletir o estado de inputs** modificados apenas em tempo de execução (ver seção "Salvando valores e persistência de dados").

## 3.3) Configurando o Gatilho por campo

- Diferente de outras fórmulas, o **retorno do gatilho não altera o valor do campo**.
- O gatilho pode **manipular o DOM do campo via JS** (por exemplo, atualizar elementos, acionar callbacks, etc.).
- As abas **Fórmula Excel** e **Fórmula integrada** **não** existem para este tipo de campo; a edição do gatilho ocorre **dentro do mesmo modal**.

---

## 4) Utilizando o Campo do tipo Desenvolvedor

## 4.1) Onde o campo aparece na interface

O campo está disponível em diversos pontos da interface:

| Componente / Local | Disponibilidade |
| --- | --- |
| **InfoWidget** (coluna esquerda das entidades) | Disponível |
| **Form** (criação/edição) e **FormMini** (inline) | Disponível |
| **DocGenerator** (modelos de proposta) | Disponível |
| **ProductSection** (modal) e **NewProductSection** (tela cheia) | Disponível |
| **Automação → Ações** | Disponível para **Administradores** |
| **Edição em Massa** | Disponível para **Administradores** |
| **DynamicTable** (abas) | **Não** disponível |
| **Filter** (filtros globais/relatórios) | **Não** disponível |
| **Reports → Dimension** (métricas) | **Não** disponível |

**NewProductSection**: semelhante ao campo multilinha, o usuário vê uma célula **“Visualizar”** que abre um modal com o campo. **Gatilhos continuam executando mesmo com o modal fechado**.

## 4.2) Salvando valores e persistência de dados

- Valores digitados em **elementos `<input>`** dentro do iframe **não são salvos automaticamente** (o estado vive apenas em memória no navegador).
- Para **persistir informações**, utilize um **callback** (por exemplo, `onchange`) que grava o valor em um elemento/estrutura persistente (ex.: um `<div>` escondido que você mesma controla) ou que **sincronize o estado** para o valor do campo quando o formulário for salvo.
- O **valor do campo** só é alterado **quando ele está presente em um formulário e o formulário é salvo no frontend**. Para atualizar registros existentes em lote, prefira **Edição em Massa** ou **Automação**.

## 4.3) Uso em Automação e Edição em Massa

- Nas telas de **Automação** e **Edição em Massa**, o botão **Configurar** permite **alterar o código** que será inserido no campo.
- **Não é possível** executar fórmulas que **dependem de valores de outros campos** nessa modalidade: a ação afeta **apenas o valor (código) do próprio campo**.

## 4.4) Exemplos práticos (padrões recomendados)

**Exemplo A – Persistindo o valor de um input**

- Estruture um `onchange` que copia o valor de um `<input>` para um `<div>` (ou outra estrutura) que você lê quando o formulário é salvo.
- Alternativamente, serialize o estado (JSON) em um nó invisível do DOM do campo para posterior leitura.

**Exemplo B – Integração com PloomesServer**

- Use **PloomesServer** para consultar/atualizar dados via API do Ploomes **sem expor chaves** no código do campo.
- Acione as chamadas em eventos do seu componente (ex.: ao clicar em **Sincronizar**).

**Exemplo C – Evite `setInterval`**

- Utilize eventos do ciclo de vida do campo (ex.: carregamento do iframe, ações do usuário, submissão do formulário) em vez de laços temporizados que continuam executando após a navegação.

---

## 5) Limitações do Campo do tipo Desenvolvedor

## 5.1) Isolamento por iframe e acesso ao DOM externo

- O campo **não** acessa diretamente o DOM do Ploomes.
- Para interagir com o DOM externo **somente na Web**, use **PloomesDocument** (indisponível no mobile).
- **Não injete código** no HTML existente do Ploomes; crie seus próprios componentes/modais dentro do iframe.

## 5.2) Comportamento no mobile

- **PloomesDocument não funciona no mobile**; a aplicação móvel possui arquitetura distinta e não expõe `document` ao campo.

## 5.3) Restrições de armazenamento e formatos

- **Inputs não persistem automaticamente**; implemente callbacks para salvar estados.
- **Imagens em Base64 são bloqueadas**.
- Códigos pesados podem **degradar performance** do CRM (evite operações custosas; libere recursos quando o usuário sair da tela).

## 5.4) Restrições de dependência entre campos

- Em **Automação** e **Edição em Massa**, **não** é possível criar fórmulas que se baseiam em **outros campos** — somente o **valor do próprio campo** é alterado.

---

## 6) F.A.Q.

**6.1) Posso usar o Campo Desenvolvedor para alterar o layout global do Ploomes?**

Não. O objetivo é criar componentes **isolados**; alterações diretas no DOM do Ploomes não são suportadas e podem quebrar após atualizações.

**6.2) Consigo acessar dados do usuário logado?**

Sim, utilize **PloomesServer** para obter `userKey` e fazer chamadas à API com segurança (sem expor credenciais no código do campo).

**6.3) Por que meu `<input>` perde o valor ao recarregar?**

Porque o estado foi mantido apenas em tempo de execução. **Implemente callbacks** para persistir o valor em um nó controlado ou sincronize o estado com o **valor do campo** no momento do salvamento.

**6.4) Por que `setInterval` é desencorajado?**

Porque o intervalo continua executando mesmo após sair da tela, competindo por CPU/memória e degradando a experiência. Prefira **eventos** e **timeouts controlados**.

**6.5) Posso usar imagens Base64?**

Não. O campo **bloqueia Base64**. Utilize URLs de imagens válidas e acessíveis.

**6.6) O gatilho substitui as fórmulas Excel/Integrada?**

Para este tipo de campo, sim: o **Gatilho por campo** centraliza a lógica e **não altera diretamente o valor** do campo; ele **manipula o DOM** do componente.

---

## 7) Glossário

- **Iframe**: elemento HTML que embute um documento dentro de outro, isolando execução/estilos.
- **Gatilho por campo**: bloco de código executado no contexto do campo; **não altera o valor** diretamente, mas pode manipular o DOM do campo.
- **PloomesServer**: classe auxiliar para executar requisições à API do Ploomes (e outras) sem expor chaves no código do campo.
- **PloomesDocument**: ponte para o `document` da página principal do Ploomes disponível **apenas na Web**; indisponível no mobile.
- **Persistência de estado**: estratégia para salvar valores de UI (ex.: inputs) além do ciclo de vida de execução do iframe.
