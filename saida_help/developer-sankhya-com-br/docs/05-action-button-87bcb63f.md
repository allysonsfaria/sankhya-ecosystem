---
id: "https://developer.sankhya.com.br/docs/05_action_button"
titulo: "🔘 Botão de Ação"
url: "https://developer.sankhya.com.br/docs/05_action_button"
atualizado_em: "2025-11-10T23:36:29.000Z"
---

# 🔘 Botão de Ação

Como adicionar botões de ação customizados em formulários e telas nativas

> 📘 **Disponibilidade**: Funcionalidade disponível a partir da versão 2.0 do Add-on Studio.

A anotação `@ActionButton` é a forma moderna e declarativa de criar botões de ação personalizados em telas do Sankhya Om. Ela permite associar uma classe Java, que executa uma lógica de negócio específica, a um botão visível no menu "Ações" da tela.

![](https://files.readme.io/a355ac953caef6a452e4fcafb480041dfc8964438dd7b232c21a099b4eb0ed19-image.png)

***

### 🤔 Para que serve?

Use um Botão de Ação quando precisar que o usuário dispare manualmente uma rotina de back-end a partir de um ou mais registros de uma tela nativa.

**Casos de uso comuns:**

* **Integrações Manuais**: Enviar dados do registro selecionado para um sistema externo (ex: "Enviar para E-commerce").
* **Geração de Relatórios/Arquivos**: Criar planilhas, PDFs ou outros documentos com base nos dados da tela (ex: "Exportar para Excel").
* **Ações em Massa**: Executar uma operação complexa para vários registros selecionados (ex: "Aprovar Lotes Selecionados").
* **Interação com Formulários**: Coletar dados adicionais do usuário através de um formulário antes de executar a lógica principal.

> 👍 Para Telas personalizadas prefira criar os botões e chamar a camada de Serviços.

***

### ⚙️ Como Funciona

Para criar um botão de ação, você precisa de uma classe Java que implemente a interface `br.com.sankhya.extensions.actionbutton.AcaoRotinaJava` e anotá-la com `@ActionButton`.

O framework do Add-on Studio se encarrega de:

1. Ler a anotação e registrar o botão na tela especificada.
2. Exibir o formulário (se definido) para o usuário.
3. Instanciar sua classe e invocar o método `doAction()`, passando o contexto da execução.
4. Gerenciar a transação de banco de dados.
5. Exibir mensagens de retorno para o usuário.

#### A Interface `AcaoRotinaJava`

Esta interface define o contrato da sua ação, contendo um único método:

* `doAction(ContextoAcao contexto)`: É aqui que toda a sua lógica de negócio será executada.

#### O `ContextoAcao`

O objeto `contexto` é seu ponto de acesso a todas as informações da execução, permitindo:

* Obter os registros selecionados na tela (`contexto.getLinhas()`).
* Acessar parâmetros preenchidos no formulário (`contexto.getParam()`).
* Definir uma mensagem de sucesso ou erro para o usuário (`contexto.setMensagemRetorno()`).

***

### 📋 Atributos da Anotação `@ActionButton`

| Atributo           | Descrição                                                                                                     | Exemplo                               |
| :----------------- | :------------------------------------------------------------------------------------------------------------ | :------------------------------------ |
| `description`      | **(Obrigatório)** O texto que aparecerá para o usuário no menu de ações.                                      | `"Aprovar Nota"`                      |
| `instanceName`     | **(Obrigatório)** O nome da entidade (instância) à qual o botão está associado.                               | `"CabecalhoNota"`                     |
| `form`             | Define um formulário que será exibido ao usuário antes de executar a ação.                                    | `@Form(...)`                          |
| `transactionType`  | Comportamento transacional. O padrão é `AUTOMATIC` (o framework gerencia a transação).                        | `TransactionType.REQUIRES_NEW`        |
| `accessControlled` | Se `true` (padrão), a visibilidade do botão dependerá das permissões de acesso do usuário à tela.             | `false`                               |
| `resourceId`       | Restringe o botão a uma tela específica através do seu ID de recurso (ex: `br.com.sankhya.core.ped.pedidos`). | `"br.com.sankhya.core.cad.parceiros"` |
| `refreshType`      | Define o que deve ser atualizado na tela após a execução. Padrão: `ITEM` (atualiza o registro atual).         | `RefreshTypeEnum.ALL`                 |

***

### 🧩 Exemplo Completo com Formulário

O exemplo abaixo demonstra um botão que exibe um formulário com diversos tipos de campos antes de executar a exportação de dados.

```java
package br.com.fabricante.addon.exemplos;

import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;
import br.com.sankhya.extensions.actionbutton.ContextoAcao;
import br.com.sankhya.studio.annotations.hooks.*;

@ActionButton(
    description = "Exportar Dados para Planilha",
    instanceName = "CabecalhoNota", // Associado à entidade de Nota
    resourceId = "br.com.sankhya.core.mov.centraldenotas", // Aparecerá apenas na Central de Notas
    form = @Form(
        fields = {
            @Field(
                name = "TIPO_ARQUIVO",
                label = "Formato",
                type = FieldType.LIST,
                required = true,
                options = {
                    @Option(value = "XLSX", label = "Excel (XLSX)"),
                    @Option(value = "CSV", label = "CSV")
                }
            ),
            @Field(
                name = "DATA_INICIAL",
                label = "Data Inicial",
                type = FieldType.DATE,
                required = true
            ),
            @Field(
                name = "INCLUIR_ITENS",
                label = "Incluir Itens da Nota?",
                type = FieldType.CHECKBOX
            )
        }
    )
)
public class ExportarDadosAction implements AcaoRotinaJava {

    @Override
    public void doAction(ContextoAcao contexto) throws Exception {
        // 1. Captura dos parâmetros do formulário
        String tipoArquivo = (String) contexto.getParam("TIPO_ARQUIVO");
        java.sql.Timestamp dataInicial = (java.sql.Timestamp) contexto.getParam("DATA_INICIAL");
        boolean incluirItens = "S".equals(contexto.getParam("INCLUIR_ITENS"));

        // 2. Lógica de negócio (ex: delegar para um @Component)
        // exportacaoService.gerarPlanilha(tipoArquivo, dataInicial, incluirItens, contexto.getLinhas());

        // 3. Feedback para o usuário
        contexto.setMensagemRetorno("Exportação iniciada para o formato: " + tipoArquivo);
        
        // Se gerasse um arquivo, poderia usar:
        // contexto.setArquivoRetorno(new File(...), "relatorio.xlsx");
    }
}
```

***

### ✨ Boas Práticas

* **Lógica em Services**: Mantenha a classe do `ActionButton` enxuta. Sua responsabilidade é orquestrar a chamada e interagir com o contexto. Delegue a lógica de negócio para classes de serviço (`@Service`).
* **Especificidade com`resourceId`** : Sempre que possível, use `resourceId` para que seu botão apareça apenas na tela desejada, evitando poluir o menu "Ações" de outras telas que usam a mesma entidade.
* **Feedback Claro**: Sempre forneça uma mensagem de retorno ao usuário com `contexto.setMensagemRetorno()`, informando se a operação foi bem-sucedida ou se ocorreu um erro.
* **Segurança**: Mantenha `accessControlled = true` para garantir que o botão respeite as permissões de acesso configuradas no sistema.

### 🚫 Anti-Patterns (O que evitar)

* **Lógica de Negócio na Action**: Evite implementar regras de negócio complexas, consultas ao banco ou chamadas a APIs diretamente dentro do método `doAction`. Isso dificulta o reuso e os testes.
* **Ações sem Feedback**: Nunca deixe o usuário sem saber o que aconteceu. Uma ação que executa em silêncio pode levar o usuário a pensar que nada ocorreu.
* **Uso para Validações ou Gatilhos**: O `ActionButton` é para ações manuais. Se você precisa de uma lógica que dispare automaticamente ao salvar, excluir ou modificar um registro, use **`@BusinessRule`** , **Listener**.
* **Nomes Genéricos**: Use descrições claras e objetivas no atributo `description`. Evite nomes como "Processar" ou "Executar" sem contexto.
