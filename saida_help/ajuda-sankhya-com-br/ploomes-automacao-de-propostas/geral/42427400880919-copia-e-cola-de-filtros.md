---
id: "42427400880919"
titulo: "Cópia e Cola de Filtros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427400880919-C%C3%B3pia-e-Cola-de-Filtros"
trilha: "PLOOMES: Automação de propostas  > Geral"
atualizado_em: "2026-08-10T18:01:22Z"
rotulos: ["sync_hc", "ploomes", "ploomes_15266432", "sync_hash_9d3e83b18c0a"]
---

# Cópia e Cola de Filtros

## 1) Sobre a funcionalidade

A **Cópia e Cola de Filtros** é uma funcionalidade do Ploomes que permite copiar a estrutura completa de um grupo de regras (E/OU) de um filtro existente, ou parte dela, e colá-la em outro filtro de destino compatível — eliminando a necessidade de recriar manualmente condições repetidas entre diferentes módulos do sistema.

Com ela, é possível copiar:

- O **filtro inteiro**
- Um **bloco de condição** (grupo E/OU)
- Uma **linha específica** de condição

A funcionalidade está disponível para **todas as contas**, sem custo adicional ou necessidade de contratar módulos extras.

```
⚠️ Atenção: A funcionalidade está disponível apenas na versão Web do Ploomes. Ela não está disponível na versão mobile.
```

---

## 2) Pré-requisitos

Para utilizar a Cópia e Cola de Filtros é necessário:

- Ter acesso ao módulo onde o filtro de **origem** está configurado
- Ter acesso ao módulo onde o filtro de **destino** será aplicado
- Garantir que origem e destino pertencem à **mesma entidade-raiz** (ex.: Cliente → Cliente, Negócio → Negócio, Proposta → Proposta)
- **Conceder permissão ao navegador** para acessar a área de transferência do computador

### 2.1) Concedendo permissão ao navegador

Para usar a Cópia e Cola de Filtros, é necessário conceder permissão ao navegador para acessar a área de transferência. Essa permissão é solicitada **na primeira vez que você tenta colar um filtro copiado** e é feita uma única vez por navegador, persistindo até que você decida alterar.

Sem essa permissão, o sistema **não conseguirá armazenar nem replicar** o filtro copiado e o botão de colar **retornará uma mensagem de erro**.

![Imagem 1: Sem essa permissão, o sistema não conseguirá armazenar nem replicar o filtro copiado e o botão de colar retornará uma…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2430960542/36522ffdc14657fd22721108f70d/image.png?expires=1786536000&signature=f9439f61d64bbeb58796977ef6943eb19c74802dfe3f48d3ba97928aa15a0f24&req=diQkFsB4nYRbW%2FMW3nq%2BgTpMQs98B%2Bs%2BsALPJYjVtVHPSnY5g%2BzGDVc4B5kY%0APff1ss3K0fsLVywlte3FTeClarE%3D%0A)

### 2.2) Como resolver problemas de permissão

Caso você tenha clicado em **"Bloquear"** em vez de **"Permitir"** quando o navegador solicitou acesso à área de transferência, não será possível colar um filtro copiado, e será exibido um aviso de erro.

Para alterar a permissão:

1. Clique no ícone ao lado da URL no navegador.
2. Selecione **"Sempre permitir que esse site veja a área de transferência"**.
3. Clique em "Concluído"
4. Recarregue a página.

![Imagem 2: Recarregue a página.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2430966423/34c93350d93a48bdf02fa585f9b5/image.png?expires=1786536000&signature=5e9b57adba51300a100105cf958d3752ccbb4a0f3f2c32e2b9b381f8db0626e5&req=diQkFsB4m4VdWvMW3nq%2BgSdQB2%2Fg2S6KTXDUp9L9Q29KnOc0AHiIkCWDNFDn%0A%2BwAC7MPIAuVnFRHecsDLpmdPYhM%3D%0A)

---

## 3) Utilizando a funcionalidade

### 3.1) Como copiar um filtro

1. Abra o filtro que deseja copiar em qualquer módulo compatível.
2. Localize o grupo de regras (bloco E/OU) ou a linha específica que quer copiar.

   1. **Copiar uma linha de filtro específica:** passe o mouse sobre a linha desejada até que o ícone de cópia seja exibido. Ao utilizar essa opção, apenas o filtro selecionado será copiado. Na colagem, ele será adicionado de forma complementar a um bloco de condições já existente no local de destino ou, caso não exista nenhum bloco, será criado automaticamente um novo bloco de condições para receber o filtro.

      [GIF animado: Imagem 3: Copiar uma linha de filtro específica: passe o mouse sobre a linha desejada até que o ícone de cópia seja exibido. Ao…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2467607019/b88db96b0c0db9bb972d6590c2c4/chrome-capture-2026-05-26.gif?expires=1786536000&signature=7e5d1723af979fe95970965db00ca1fa969f58e4b51ed0237c8af1f51fa8a644&req=diQhEc9%2BmoFeUPMW3nq%2BgSWZa5ap1D0A%2FvWGn8sASzSOPg6ENUTjTtfm5jym%0Az7sl0dxKGKGFp1Vl1pNt1fHGZEY%3D%0A)
   2. **Para copiar um filtro inteiro:** utilize o ícone de cópia indicado abaixo. Ao selecionar essa opção, serão copiados todos os blocos de condições apresentados, preservando toda a estrutura do filtro.

      ![Imagem 4: Para copiar um filtro inteiro: utilize o ícone de cópia indicado abaixo. Ao selecionar essa opção, serão copiados todos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2467626804/b84efe64e3729ff0a8f9cd877240/image.png?expires=1786536000&signature=d0fbebafde48a7850ffde57f5e33dfb4775754cba7d896058c7d511193b1ea53&req=diQhEc98m4lfXfMW3nq%2Bgd6yUxGp1HaI7%2FljVhboOoGL%2BqmRHeJVB2jdQmo%2B%0Aj2MSrk9gHOCtGmNJAf%2F26reOCO0%3D%0A)

      ```
      Observação: Ao colar um filtro inteiro, todos os blocos de condições e critérios já existentes no local de destino serão substituídos pelo conteúdo copiado. Essa ação sobrescreve a configuração atual, preservando apenas a estrutura do filtro colado.
      ```
   3. **Para copiar um bloco de condições:** A cópia de um bloco de condições permite copiar todos os filtros e critérios configurados dentro daquela condição, e, ao ser colado, o bloco é adicionado aos blocos de condições já existentes no local de destino, complementando a configuração atual sem substituir as demais condições.

      ![Imagem 5: Para copiar um bloco de condições: A cópia de um bloco de condições permite copiar todos os filtros e critérios…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2467637099/dca2dcb322836344d9308b8d6920/image.png?expires=1786536000&signature=916f7b6c00bfa75f55595875685e9d7608cd9b89a0b067920b220cff421d8365&req=diQhEc99moFWUPMW3nq%2BgTSOQKvgL0D4xIE6QQ7gF5TANrbR6AQ5pebXsHfd%0AOJKzMWrnKiuOdnTodJZ%2BRUi1zUU%3D%0A)
3. Clique no ícone **"Copiar"** ao lado do filtro/grupo de filtro desejado.
4. Uma mensagem **de confirmação** será exibida, indicando que o filtro foi copiado para a área de transferência.

O filtro copiado fica armazenado na **Clipboard do computador** e persiste enquanto a sessão do navegador estiver aberta.

---

### 3.2) Como colar um filtro

1. Navegue até o módulo de destino onde deseja aplicar o filtro copiado.
2. Abra o painel de filtros do destino.
3. Clique no ícone **"Colar"** disponível no painel de filtros.
4. O(s) filtro(s) copiado(s) será adicionado como um **bloco adicional no topo** (OU), sem sobrescrever as condições já existentes.

**Importante sobre o comportamento da colagem:**

- Em um **filtro vazio**: a estrutura copiada é aplicada integralmente.
- Em um **filtro preenchido**: o conteúdo copiado é acrescentado como novo bloco/linha, sem destruir o que já existia.

```
⚠️ O ícone "Colar" só fica disponível quando há um filtro/grupo de filtros previamente copiado na área de transferência. Se o clipboard estiver vazio, o ícone não será exibido em nenhum filtro.

ℹ️ O filtro colado é uma cópia independente. Alterações feitas no filtro original após a colagem não serão refletidas no destino.
```

---

### 3.3) Contextos suportados

A Cópia e Cola de Filtros funciona nos seguintes módulos como **origem e destino**:

| Filtros de abas |
| --- |
| Filtros de relatórios |
| Filtros de metas |
| Filtros de automações |
| Filtros em checklist |
| Filtros em fluxo de aprovação |
| Filtros em fórmula de campo (Campos selecionáveis: Usuário, Produto, Cliente, Símbolo de moeda) |
| Filtros na integração Sankhya |

---

## 4) Regras de compatibilidade

Para garantir que o filtro colado funcione corretamente, o Ploomes aplica uma validação de entidade entre origem e destino:

| Origem | Destinos permitidos | Destinos incompatíveis |
| --- | --- | --- |
| Cliente | Filtros de Cliente | Negócio, Proposta, etc. |
| Negócio | Filtros de Negócio | Cliente, Proposta, etc. |
| Proposta | Filtros de Proposta | Cliente, Negócio, etc. |

**Regra geral:** O filtro só pode ser colado em destinos cuja entidade-raiz seja a mesma da origem. Ao tentar colar em um destino incompatível, o sistema exibirá uma mensagem de erro.

### 4.1) Mensagens de erro

**Ao tentar colar em entidade incompatível:**

Será exibida uma mensagem de erro com a mensagem: **"Filtro copiado é incompatível com esta entidade."** Nenhuma alteração é feita no filtro de destino.

**Ao tentar colar algo que não corresponde a um filtro:**

Caso o ícone de colar seja exibido por inconsistência e você tente colar algo que não é um filtro, um toast de erro explicativo será exibido e nenhuma alteração é feita no filtro de destino.

### 4.2) Persistência da área de transferência

- ✅ Persiste entre abas da mesma sessão do navegador
- ❌ Não persiste após fechar o navegador
- ❌ Não sincroniza entre dispositivos diferentes

---

## 5) Limitações

- **Não está disponível na versão mobile.** A funcionalidade de copiar e colar grupos de filtro funciona apenas na versão Web do Ploomes.
- **Não é uma biblioteca de filtros salvos.** Não há listagem, nomeação ou histórico de filtros copiados — apenas o **último item copiado** fica disponível no clipboard.
- **Não é um link vivo.** Editar o filtro original após copiar ou colar **não propaga mudanças** para o destino.
- **Não é multi-clipboard.** Apenas **um grupo de regras** pode estar na área de transferência por vez; uma nova cópia substitui a anterior imediatamente.
- **Não substitui o conteúdo do destino.** O filtro copiado é sempre adicionado como **bloco adicional**, nunca sobrescreve regras existentes.
- **Sem versionamento.** Não há histórico de qual filtro foi colado em qual lugar.

---

## 6) F.A.Q.

### 6.1) Posso copiar um filtro de Negócio e colar em um filtro de Cliente?

Não. A compatibilidade de entidade é estrita. O filtro só pode ser colado em destinos que compartilhem a **mesma entidade-raiz** que a origem. Ao tentar colar em uma entidade diferente, o sistema exibirá um aviso de incompatibilidade.

### 6.2) Por que os botões de copiar e colar não estão aparecendo?

Provavelmente o navegador não tem permissão para acessar a área de transferência. Verifique se você concedeu permissão de clipboard ao acessar o Ploomes — caso tenha clicado em "Bloquear" por engano, é possível alterar nas configurações do site (veja o item 2.2 deste artigo).

### 6.3) O filtro copiado fica salvo se eu fechar o navegador?

Sim. O filtro fica armazenado na **Clipboard do computador** e é mantido mesmo ao fechar o navegador. Ele persiste inclusive entre abas abertas simultaneamente.

### 6.4) Se eu editar o filtro original depois de colar, as mudanças aparecem no destino?

Não. A colagem gera uma **cópia independente**. Qualquer alteração feita no filtro de origem após a colagem não é refletida nos destinos onde ele já foi colado.

### 6.5) Posso ter mais de um filtro copiado ao mesmo tempo?

Não. O clipboard suporta apenas **um grupo de regras por vez**. Ao copiar um novo filtro, o anterior é substituído automaticamente.

### 6.6) A funcionalidade está disponível no app Ploomes?

Não. A Cópia e Cola de Filtros está disponível **apenas na versão Web** do Ploomes.

### 6.7) O que acontece com o filtro já existente no destino quando eu colo um novo filtro?

O novo filtro vai sobrepor todo o filtro existente. Essa ação só poderá ser desfeita caso você não salve as alterações.

![Imagem 6: O novo filtro vai sobrepor todo o filtro existente. Essa ação só poderá ser desfeita caso você não salve as alterações.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2431062470/1602ce4522e2e309f796dc21f79e/image.png?expires=1786536000&signature=69e04b4e9de21eceb92cb1dd05cface86b0ba2107f5b8feb1592232d46687ea6&req=diQkF8l4n4VYWfMW3nq%2BgZ0aOtyjuPZBdcZZlTVJPIWFtM5FfKaFn4exSltu%0Ajtlr7PyHaRj5onKdL2qRifqA4uU%3D%0A)

### 6.8) O que acontece quando colo um bloco de condições de filtro?

O filtro copiado é adicionado como um novo bloco (OU) no filtro de destino. As condições já existentes não são removidas nem sobrescritas.

![Imagem 7: O filtro copiado é adicionado como um novo bloco (OU) no filtro de destino. As condições já existentes não são…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2431064539/2e97f7158c7a97c501c45c11b62d/image.png?expires=1786536000&signature=03217324eac25569522cd21d1db1b77ea4f29bcfc3540eec8776e68d2d7a5c17&req=diQkF8l4mYRcUPMW3nq%2BgfMXGf7ISqqNd9Y3Quu133msrlglKl3868MMkZxo%0Amc1038Rc612qjLwJav2HoQ9ndMw%3D%0A)

### 6.9) O que acontece com as linhas de filtro já existentes no destino quando eu colo uma nova linha?

Ela é adicionada de forma complementar ao bloco de condições

![Imagem 8: Ela é adicionada de forma complementar ao bloco de condições](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2431081361/cf08834df58b06c4439a9a05d4f1/image.png?expires=1786536000&signature=685f3beaf1ce2b274248ea83709ea5628e4cbb2f37005cb5bc3a00738ac27b86&req=diQkF8l2nIJZWPMW3nq%2Bgei%2FJzfvbFLUchF2gNe5sp5UJrXhVgE4OUcMZQ88%0AsJvd%2BouNls5u3guTGfvwoCzBPUU%3D%0A)

---

## 7) Dicas adicionais

- **Reutilize filtros complexos:** Use a Cópia e Cola para reaproveitar grupos de regras elaborados em relatórios, metas e automações sem precisar reconfigurar do zero.
- **Padronize condições entre módulos:** Se sua empresa usa critérios de segmentação consistentes (ex.: região, status, responsável), copie o grupo de regras uma vez e distribua para todos os filtros relacionados.
- **Cuidado com o clipboard:** Lembre-se de que apenas o último filtro copiado fica disponível. Se precisar colar o mesmo filtro em vários destinos, faça todas as colagens antes de copiar outro filtro.
- **Verifique a entidade antes de colar:** Antes de iniciar o processo, confirme que o filtro de destino pertence à mesma entidade da origem para evitar erros de incompatibilidade.

---

## 8) Glossário

- **Bloco de condições (E/OU):** Conjunto de regras dentro de um filtro que agrupa critérios com os operadores lógicos E (todas as condições devem ser verdadeiras) ou OU (ao menos uma condição deve ser verdadeira).
- **Entidade-raiz:** A entidade principal que o filtro está configurado para avaliar, como Cliente, Negócio ou Proposta.
- **Clipboard:** Área de transferência do computador onde o filtro copiado fica armazenado temporariamente durante a sessão do navegador.
- **Bloco adicional (OU):** Quando um bloco é colado, ele é inserido como um novo grupo de condições conectado pelo operador OU ao conjunto de regras já existente no destino.
