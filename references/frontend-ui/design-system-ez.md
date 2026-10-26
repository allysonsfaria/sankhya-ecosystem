# Sankhya Design System (Componentes ez-*)

O Sankhya Design System fornece componentes web modernos para customizações e telas de Addon Studio integradas à interface nativa do Sankhya OM.

---

## 1. Principais Componentes (ez-*)

| Componente | Função |
|---|---|
| `<ez-grid>` | Grade de dados rica com suporte a ordenação, paginação e seleção |
| `<ez-form>` | Contêiner de formulário com gerenciamento de estado |
| `<ez-text-input>` | Campo de entrada de texto com validação e máscara |
| `<ez-number-input>` | Campo numérico com formatação decimal e moeda |
| `<ez-date-input>` | Seletor de data e calendário nativo |
| `<ez-combo-box>` | Seleção suspensa com carregamento sob demanda |
| `<ez-button>` | Botões com estilos padronizados (primário, secundário, perigo) |
| `<ez-modal>` | Janelas modais e diálogos de confirmação |
| `<ez-toast>` / `<ez-alert>` | Mensagens flutuantes de feedback ao usuário |

---

## 2. Padrão DataUnit (Abstração de CRUD Frontend)

O `DataUnit` gerencia a comunicação entre os componentes da interface e o backend do Sankhya:

```html
<ez-grid id="gridParceiros" 
         data-unit="parceirosUnit"
         selection-mode="single">
</ez-grid>
```

```javascript
const grid = document.getElementById('gridParceiros');

// Configuração de colunas
grid.setColumnsDef([
    { field: 'CODPARC', title: 'Cód.', width: 80 },
    { field: 'NOMEPARC', title: 'Nome / Razão Social', width: 250 },
    { field: 'CGC_CPF', title: 'CPF/CNPJ', width: 140 },
    { field: 'CODCID', title: 'Cidade', width: 100 }
]);

// Carregamento de dados via DataUnit
const unit = new DataUnit('Parceiro');
unit.loadRecords({
    criteria: "this.ATIVO = 'S'"
}).then(dados => {
    grid.setData(dados);
});
```

---

## 3. Diretrizes de Layout e Estilo (Acorde)
- Utilize as classes utilitárias de espaçamento e flexbox do Design System para respeitar a densidade de pixels do ERP.
- Mantenha conformidade com temas claro e escuro fornecidos pela casca do Sankhya OM.
