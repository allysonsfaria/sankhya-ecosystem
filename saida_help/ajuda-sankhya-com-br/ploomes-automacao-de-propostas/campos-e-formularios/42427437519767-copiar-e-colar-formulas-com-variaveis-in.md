---
id: "42427437519767"
titulo: "Copiar e Colar fórmulas com variáveis inseridas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427437519767-Copiar-e-Colar-f%C3%B3rmulas-com-vari%C3%A1veis-inseridas"
trilha: "PLOOMES: Automação de propostas  > Campos e formulários"
atualizado_em: "2026-08-10T18:02:29Z"
rotulos: ["sync_hc", "ploomes", "ploomes_13945526", "sync_hash_ca6c5215ea36"]
---

# Copiar e Colar fórmulas com variáveis inseridas

## 1) Sobre a funcionalidade

Configurar fórmulas complexas exige precisão e, muitas vezes, a repetição de lógicas entre diferentes campos. Para tornar esse processo mais ágil e menos suscetível a erros manuais, o Ploomes agora permite que você copie e cole trechos de fórmulas mantendo a integridade das variáveis. Além disso, introduzimos um atalho de teclado que elimina a necessidade de usar o mouse para buscar campos, permitindo que você escreva suas fórmulas de forma contínua e fluida.

---

## 2) Pré-requisitos

- **Permissão de Edição:** É necessário ter autorização para edição de campos da conta (Administração).
- **Módulo CPQ:** Para copiar e colar fórmulas entre campos que pertençam ao módulo de CPQ (propostas e orçamentos), é necessário que sua conta tenha este módulo contratado. No plano Ploomes Básico, a funcionalidade é restrita aos campos nativos e customizados de outras entidades (Clientes, Produtos, etc.).

---

## 3) Copiando e Colando Fórmulas

Agora, o editor de fórmulas do Ploomes reconhece metadados das variáveis, garantindo que elas sejam reconstruídas corretamente ao serem transportadas.

### 3.1) Entre editores do Ploomes (Colagem Inteligente)

Ao copiar um trecho de fórmula dentro do Ploomes, o sistema armazena não apenas o texto, mas a referência exata de cada campo utilizado.

1. Selecione o texto ou a variável desejada no editor de origem.
2. Pressione `Ctrl+C` (Windows) ou `Cmd+C` (Mac).
3. No editor de destino, pressione `Ctrl+V` (Windows) ou `Cmd+V` (Mac).
4. O sistema colará o texto e reconstruirá as variáveis automaticamente.
5. **Confirmação:** Um aviso (toaster) de sucesso aparecerá no canto da tela informando que as variáveis foram coladas com sucesso.

![Imagem 1: Confirmação: Um aviso ( toaster ) de sucesso aparecerá no canto da tela informando que as variáveis foram coladas com…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2131758415/5926d4fe34df58ea968f3d3b27ce/image+%2834%29.png?expires=1786536000&signature=36eead6b94fa3bb9f7af2f8de770a6f40dc4bc6ebeb705d9e47773dbc09d6d08&req=diEkF857lYVeXPMW3nq%2BgdR3cMqmm8e18XRzb8pcjehE9NnVDDadzuU%2BPEpk%0AkMEEIdfN%2B%2BRLve9S%2B2X4wiXJa9I%3D%0A)

### 3.2) Conteúdo de fontes externas

Você também pode trazer fórmulas de ferramentas externas (como Notion, Discord ou Bloco de Notas).

- O Ploomes tentará identificar variáveis de **primeiro nível** no texto colado.
- **Importante:** Atualmente, a colagem externa não suporta o "descer entidades" nos field paths. Ou seja, apenas campos diretos da entidade serão reconhecidos. Caso o sistema encontre uma estrutura que não consiga mapear, ele exibirá um alerta.

---

## 4) Atalho "#" para inserir variáveis

Para ganhar velocidade na escrita, você não precisa mais abrir o seletor de campos com o mouse.

1. Com o cursor dentro do editor de fórmulas, digite o caractere `#`.
2. Um seletor de campos abrirá instantaneamente na posição do seu cursor.
3. Utilize as **setas do teclado** (↑/↓) para navegar entre as opções.
4. Pressione **Enter** para confirmar a inserção do campo escolhido.
5. Caso queira desistir da inserção, pressione **Esc** para fechar o seletor.

[GIF animado: Imagem 2: Caso queira desistir da inserção, pressione Esc para fechar o seletor.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2131760088/eb408783b42e6c7d119ce13ac088/gif+copiar+e+colar.gif?expires=1786536000&signature=47538c07c95082b48295e5c1890a7e9f1316d4f300bc8716cc20a61d8c2d39c7&req=diEkF854nYFXUfMW3nq%2BgQCTW1vzreJ3%2BOA%2FY6iqnBcRY11S4BGdFs65H71N%0A1WH9WHRvycDMTcYubYJk%2BFo%2Fm7g%3D%0A)

---

## 5) Limitações

- **Variáveis Externas:** Ao colar fórmulas de fontes fora do Ploomes, o sistema reconhece apenas variáveis de primeiro nível. Caminhos complexos que envolvem múltiplas entidades vinculadas não serão reconstruídos automaticamente nesta modalidade.
- **Mapeamento entre Entidades:** Se você copiar uma variável de um formulário de "Clientes" e tentar colar em um formulário de "Produtos", por exemplo, o sistema poderá não encontrar o campo correspondente devido à diferença de contexto entre as entidades.
- **Campo "Sua Empresa":** O campo "Sua Empresa" não está disponível no novo seletor de campos (ativado pelo atalho `#`). No seletor de campos fora do editor de fórmulas, ele continua aparecendo normalmente. Essa limitação já está mapeada internamente para correção. Enquanto isso, caso você precise referenciar dados de "Sua Empresa" em uma fórmula, utilize o seletor de campos disponível fora do editor.

---

## 6) F.A.Q.

**O que acontece se eu colar uma variável que não existe no campo de destino?** O Ploomes substituirá a variável pelo texto `[[Campo.NOME_DA_VARIAVEL_NAO_ENCONTRADA]]` (mantendo o nome original para sua referência). Um alerta será exibido avisando que nem todos os campos foram mapeados. Você precisará ajustar manualmente essa variável antes que a fórmula funcione corretamente.

**Posso salvar uma fórmula que contenha variáveis "Não Encontradas"?** Sim, o sistema não bloqueia o salvamento. No entanto, ele emitirá um alerta visual para que você saiba que a fórmula está inconsistente e pode não retornar os valores esperados.

**O atalho "#" funciona em qualquer campo de texto do Ploomes?** Não. O atalho é exclusivo para os editores de fórmulas (Fórmulas simples, integradas e condicionais) em áreas de configuração de campos, funis e modelos de documentos.

---

## 7) Dicas adicionais para melhores resultados

- **Atenção aos Alertas:** Sempre verifique o canto superior da tela após colar uma fórmula. O Ploomes indica exatamente se a operação foi 100% bem-sucedida ou se algo precisa de sua revisão.
- **Uso do Teclado:** Tente realizar uma configuração completa usando apenas as setas, o `#` e o `Enter`. Isso reduz drasticamente o tempo de criação de fórmulas extensas.

---

## 8) Glossário

- **Variable (Variável):** Representação de um campo do sistema (como "Nome do Cliente") dentro de uma fórmula.
- **Fieldpath:** O caminho técnico que o sistema percorre para encontrar uma informação (ex: `Cliente > Endereço > Cidade`).
- **Toaster:** Pequenas mensagens de notificação que aparecem e desaparecem rapidamente no topo ou canto da interface.
