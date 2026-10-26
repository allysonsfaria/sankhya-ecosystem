---
id: "38955786766103"
titulo: "Bia Compose: Customização de ERP via Inteligência Artificial "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38955786766103-Bia-Compose-Customiza%C3%A7%C3%A3o-de-ERP-via-Intelig%C3%AAncia-Artificial"
trilha: "Manual do Produto > Inteligência e Análise > BIA - Business Intelligence Assistant > Bia Compose"
atualizado_em: "2026-07-29T16:03:50Z"
rotulos: ["Configuração", "Sankhya ID", "customização", "BIA", "IA", "Inteligência Artificial", "ERP", "Bia Compose"]
---

# Bia Compose: Customização de ERP via Inteligência Artificial 

O **Bia Compose** é a ferramenta de vibecoding da Sankhya que permite a usuários técnicos e administradores customizarem o ERP de forma intuitiva.

Através de comandos em linguagem natural (conversa no chat), você pode criar novas telas de cadastro e gerar dashboards complexos sem a necessidade inicial de codificação manual ou conhecimento profundo de SQL.

---

## Valor para o negócio

- **Agilidade Extrema:** reduz drasticamente o tempo de criação de telas simples e prototipagem.
- **Autonomia Técnica:** permite que administradores realizem manutenções e criem indicadores sem depender constantemente de desenvolvedores.
- **Redução de Erros:** a Bia consulta automaticamente o Dicionário de Dados e gera a query SQL correta, minimizando falhas de lógica.
- **Visualização em Tempo Real:** as alterações aparecem instantaneamente, permitindo validar o resultado sem precisar de recargas de página (F5).

---

## Pré-requisitos

Antes de iniciar, certifique-se de cumprir os seguintes itens:

- [ ] **Sankhya ID:** possuir uma conta ativa.
- [ ] **Módulo Habilitado:** o Bia Compose deve estar ativo em seu contrato.
- [ ] **Permissões de Rotina:** Seu usuário deve ter acesso às telas:
  - Construtor de Telas;
  - Construtor de Dashboard;
  - Construtor de Componente de BI.

---

## Configuração inicial:

### Liberação no Bia Studio

Para que a Bia entenda que você é um "criador", siga estes passos:

1. Acesse a tela **Acessos** e libere a rotina **Bia Studio** para o administrador.
2. No **Bia Studio**, localize o grupo **"Bia Compose"**.
3. Adicione o e-mail do usuário que será responsável pela criação dos conteúdos.
4. **Atualização:** recarregue a página do ERP para que os agentes (Construtor de Tela/Dashboard) apareçam no chat da Bia.

---

## Criando dashboards inteligentes

Os dashboards são focados em visualização de dados. Diferente das telas, eles **não possuem etapa de publicação**.

1. **Inicie o Agente:** no chat da Bia, selecione o agente **Construtor de Dashboard**.
2. **Faça o Pedido:** solicite o indicador usando termos de negócio.
   - Exemplo: "Bia, crie um gráfico de pizza com o total de vendas por região no mês atual."
3. **Processamento:** a Bia consultará o Dicionário de Dados, gerará a query SQL e montará o layout automaticamente.
4. **Resultado:** a Bia criará os Componentes de BI, o Dashboard e o Lançador de Menu. Clique em **Abrir Tela** para visualizar.

---

### Componentes suportados (Base HTML)

| **Componente** | **Descrição** |
| --- | --- |
| **Gráfico de Barras** | Ideal para comparações entre categorias. |
| **Tabela** | Visualização detalhada de registros. |
| **Gráfico de Linhas** | Evolução temporal de indicadores. |
| **Gráfico de Pizza** | Distribuição proporcional de dados. |

---

## Criando e editando telas

### 1. Criando uma nova tela (mestre e detalhe)

Basta descrever sua necessidade no chat.

- **Exemplo:** "Crie uma nova tela mestre chamada 'Cadastro de Projetos' com os campos: Nome (texto), Responsável (texto) e Prazo (data)."
- A Bia criará o **"Lançador de Menu"** e liberará o acesso automaticamente.

### 2. Editando e turbinando

Você pode solicitar ajustes em telas já criadas pela Bia:

- "Mude o campo Email para obrigatório."
- "Adicione um filtro no campo Parceiros."

### 3. Publicando a tela (Regra de Ouro ⚠️)

Toda tela nasce como **Rascunho** (limitada a 5 registros para teste).

- Para uso em produção: acesse **Configurações Telas Bia** e clique em **Publicar**.
- **Atenção:** uma tela **Publicada** não pode mais ser editada via chat pela Bia.

---

## O Ponto de não retorno: edição manual

Esta é a regra mais importante para manter a inteligência da sua assistente:

- **Vínculo com a Bia:** enquanto você editar via chat, a Bia mantém o controle total do componente.
- **Quebra de Vínculo:** se você abrir o Construtor (Telas, Dashboards ou BI) e fizer qualquer alteração manual no código ou layout, **a Bia perderá permanentemente a capacidade de editar esse item.**

**Por que isso acontece?** isso evita que a IA sobrescreva configurações técnicas complexas ou scripts personalizados que ela não conseguiria interpretar com segurança.

---

## Resolução de problemas

- **Limites de Licença:** dashboards consomem licenças de "Análise". Caso ocorra erro de licença, consulte seu Gerente de Contas.
- **A Bia não obedece mais:** verifique se a tela já foi **Publicada** ou se sofreu **Edição Manual**. Nestes casos, o ciclo da Bia para esse item foi encerrado.
- **Dados Incorretos:** se o SQL gerado parecer errado, não ajuste manualmente. Peça à Bia: "Bia, ajuste a query para filtrar apenas pedidos com status 'P' (Confirmados)."
