---
id: "42948757273367"
titulo: "Cottonbaby - Motivo de descontos (Personalização)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948757273367-Cottonbaby-Motivo-de-descontos-Personaliza%C3%A7%C3%A3o"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T16:50:31Z"
rotulos: ["sync_hc", "vidya", "vidya_527241", "sync_hash_e8f5e13ed635"]
---

# Cottonbaby - Motivo de descontos (Personalização)

**Vídeo apresentação: <https://drive.google.com/file/d/1qrpqYSX8MVjRWzK67orGJ8J1_bNRkK9O/view?usp=sharing>**

A Cottonbaby possui um sistema de personalização de descontos que opera de maneira integrada entre o sistema web e o aplicativo, com foco em garantir flexibilidade nas políticas comerciais e controle interno dos valores aplicados. Vamos detalhar cada parte desse processo.

**Obs:** Os vendedores possuem 3 cadastros de vendedores, 1 como o seu próprio gerente e 2 separados em segmentos de produtos.

##

## 1. Interface de Descontos

![Imagem 1: 1. Interface de Descontos](https://ajuda.sankhya.com.br/hc/article_attachments/42957157190551)![Imagem 2: 1. Interface de Descontos](https://ajuda.sankhya.com.br/hc/article_attachments/42957186578583)![Imagem 3: 1. Interface de Descontos](https://ajuda.sankhya.com.br/hc/article_attachments/42957173968279)![Imagem 4: 1. Interface de Descontos](https://ajuda.sankhya.com.br/hc/article_attachments/42957187146007)

Na interface do sistema, há um botão chamado **"Motivo de Desconto"**, disponível tanto no aplicativo quanto no web. Esse botão permite selecionar motivos pré-configurados que influenciam a aplicação de descontos.

- **Nota Fiscal:** Aplica o desconto ao pedido completo.
- **Item Específico:** Aplica o desconto diretamente em um item do pedido.

Mesmo com o desconto configurado, o valor final do pedido permanece o mesmo visualmente. O desconto é enviado internamente para controle do sistema na tela **Descontos Vidya**.
![Imagem 5: Mesmo com o desconto configurado, o valor final do pedido permanece o mesmo visualmente. O desconto é enviado…](https://ajuda.sankhya.com.br/hc/article_attachments/42957170787735)![Imagem 6: Mesmo com o desconto configurado, o valor final do pedido permanece o mesmo visualmente. O desconto é enviado…](https://ajuda.sankhya.com.br/hc/article_attachments/42957171132695)

### Detalhes exibidos incluem:

- Código da política comercial
- Empresa vinculada
- Perfil do cliente
- Porcentagem máxima permitida
- Tipo de lançamento (nota ou item)
- Motivo do desconto
- Valor do desconto

##

## 2. Tela de Políticas Comerciais

Para que os descontos apareçam e funcionem corretamente, é necessária uma configuração prévia na tela de **Políticas Comerciais**. Essa configuração segue uma hierarquia em cascata por empresa.

![Imagem 7: Para que os descontos apareçam e funcionem corretamente, é necessária uma configuração prévia na tela de Políticas…](https://ajuda.sankhya.com.br/hc/article_attachments/42957171388311)![Imagem 8: Para que os descontos apareçam e funcionem corretamente, é necessária uma configuração prévia na tela de Políticas…](https://ajuda.sankhya.com.br/hc/article_attachments/42957159198999)

- Se o cliente pertence à empresa vinculada, a política da empresa é aplicada.
- Se não pertence, o sistema busca a política nas demais configurações ativas.

### Filtros aplicáveis:

- **Perfil do Cliente:** Exemplo: Atacado Alimentar.
- **Regional do Vendedor:** Apenas vendedores vinculados a regiões permitidas podem aplicar descontos.

Se ambos os filtros forem validados, o sistema segue para a etapa de definição dos motivos e porcentagens de desconto.

##

## 3. Motivos de Desconto

![Imagem 9: 3. Motivos de Desconto](https://ajuda.sankhya.com.br/hc/article_attachments/42957175648407)

![Imagem 10: 3. Motivos de Desconto](https://ajuda.sankhya.com.br/hc/article_attachments/42957218230551)

Cada empresa pode ter diferentes motivos de desconto configurados. Esses motivos podem estar ativos ou inativos e são classificados como:

- **Desconto por Nota:** Aplica-se ao valor total.
- **Desconto por Item:** Aplica-se a itens específicos.

Os motivos também possuem uma porcentagem máxima configurada. Exemplo: "Pagamento à Vista" com até 2% de desconto.

### Tipos de Liberação:

A concessão do desconto depende do nível hierárquico do colaborador:

![Imagem 11: A concessão do desconto depende do nível hierárquico do colaborador:](https://ajuda.sankhya.com.br/hc/article_attachments/42957176197399)

- **Representante:** Exemplo: Pode conceder até 80% da porcentagem configurada.
- **Supervisor:** Exemplo: Concede entre 80% e 100%.
- **Gerente Nacional:** Exemplo: Pode conceder até 100% ou mais, sujeito à liberação extra.

Se o representante exceder o limite, o pedido entra em um fluxo de aprovação para análise interna.

**Obs:** A porcentagem inicial e final das liberações do tipo de liberador é baseado na porcentagem de desconto dos **Motivos da Política**, exemplo: o motivo da política possui 3% de desconto, e o representante possui 1% dentro dos 3%.

##

## 4. Grupos de Produtos e Itens Específicos

O sistema permite configurar descontos para produtos ou grupos de produtos específicos. Para isso:

- **Grupo de Produtos:** Exemplo: "Hastes Flexíveis". O desconto é aplicado ao grupo inteiro.
- **Produto Específico:** Exemplo: "Absorvente", o desconto é vinculado somente a este item.

Essa configuração só é válida para **Descontos por Item**. Se configurada como **Desconto por Nota**, nada será alterado.
