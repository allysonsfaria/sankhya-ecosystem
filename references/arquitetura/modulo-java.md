# Módulo Java Clássico (JAR / Extensões Legadas)

Para extensões que não utilizam o Addon Studio 2.0 (JARs compilados manualmente e adicionados nas pastas do servidor ou tela Módulos Java do Sankhya OM).

## Diferenças Principais em Relação ao Addon Studio
- Sem anotações `@ActionButton`, `@Listener` e `@Job` automáticas; os vínculos são feitos via arquivos de configuração XML ou diretamente no Dicionário de Dados / Construtor de Telas / Ações Personalizadas.
- O pacote compilado é empacotado em `.jar` contendo `META-INF/manifest.mf` ou descritores compatíveis.

## 1. Botão de Ação Java no Módulo Clássico
A classe implementa `AcaoRotinaJava` da mesma forma, porém é cadastrada no Sankhya pelo Dicionário de Dados > Ações:

```java
package br.com.empresa.modulo;

import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;
import br.com.sankhya.extensions.actionbutton.ContextoAcao;
import br.com.sankhya.extensions.actionbutton.Registro;

public class AcaoCustomizada implements AcaoRotinaJava {
    @Override
    public void doAction(ContextoAcao ctx) throws Exception {
        Registro[] registros = ctx.getLinhas();
        for (Registro r : registros) {
            // manipular dados
        }
        ctx.setMensagemRetorno("Operação finalizada.");
    }
}
```

## 2. Evento Java de Tabela (EventoGeral / EventoProgramavelJava)
Registrado no Dicionário de Dados na aba **Eventos**:
- Classe: pacote completo (ex: `br.com.empresa.modulo.ValidadorNotaEvento`)
- Eventos: Antes de Salvar, Depois de Salvar, Antes de Excluir, etc.

```java
package br.com.empresa.modulo;

import br.com.sankhya.jape.event.PersistenceEvent;
import br.com.sankhya.jape.event.TransactionListener;
import br.com.sankhya.jape.vo.DynamicVO;

public class EventoPersistenciaTabela implements TransactionListener {
    @Override
    public void beforeInsert(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        // regras de validação
    }

    @Override
    public void beforeUpdate(PersistenceEvent event) throws Exception {
        DynamicVO vo = (DynamicVO) event.getVo();
        DynamicVO oldVo = (DynamicVO) event.getOldVO();
    }

    @Override
    public void beforeDelete(PersistenceEvent event) throws Exception {}

    @Override
    public void afterInsert(PersistenceEvent event) throws Exception {}

    @Override
    public void afterUpdate(PersistenceEvent event) throws Exception {}

    @Override
    public void afterDelete(PersistenceEvent event) throws Exception {}

    @Override
    public void beforeCommit(TransactionEvent event) throws Exception {}

    @Override
    public void afterCommit(TransactionEvent event) throws Exception {}

    @Override
    public void afterRollback(TransactionEvent event) throws Exception {}
}
```

## 3. Regra de Negócio de Confirmação de Nota
Configurada no Cadastro de Tipos de Operação (TOP) ou no Construtor de Telas.
Interface: `br.com.sankhya.modelcore.comercial.Regra` ou chamada via interceptor de faturamento.
