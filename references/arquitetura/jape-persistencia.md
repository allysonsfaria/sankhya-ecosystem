# JAPE — Framework de Persistência Sankhya

O JAPE (Java Application Persistence Engine) é o ORM corporativo do ERP Sankhya.

## 1. Controle de Sessão e Transação (Obrigatório)

Toda manipulação de dados deve rodar em bloco seguro `JapeSession`:

```java
SessionHandle hnd = null;
try {
    hnd = JapeSession.open();
    hnd.execWithTX(new JapeSession.TXBlock() {
        @Override
        public void doWithTx() throws Exception {
            // Operações JAPE ou NativeSql aqui
        }
    });
} finally {
    JapeSession.close(hnd);
}
```

### Transação Autônoma (Autonomous TX)
Utilizada para auditoria, gravação de logs ou operações que não devem sofrer rollback caso a transação principal falhe:

```java
hnd.execWithAutonomousTX(new JapeSession.TXBlock() {
    @Override
    public void doWithTx() throws Exception {
        // commit imediato e independente
    }
});
```

### Evitar Timeout em Processos Longos
```java
hnd.setCanTimeout(false);
```

---

## 2. DynamicVO e JapeFactory (Acesso Canônico)

### Inserir Registro:
```java
JapeWrapper dao = JapeFactory.dao(DynamicEntityNames.PARCEIRO); // "Parceiro"
DynamicVO parceiroVO = dao.create()
    .set("NOMEPARC", "Cliente Exemplo LTDA")
    .set("TIPPESSOA", "J")
    .set("CGC_CPF", "12345678000199")
    .set("CODCID", new BigDecimal(1))
    .save();

BigDecimal codParc = parceiroVO.asBigDecimal("CODPARC");
```

### Consultar por Chave Primária:
```java
JapeWrapper dao = JapeFactory.dao(DynamicEntityNames.CABECALHO_NOTA); // "CabecalhoNota"
DynamicVO cabVO = dao.findByPK(nuNota);
if (cabVO != null) {
    BigDecimal vlrNota = cabVO.asBigDecimal("VLRNOTA");
    Timestamp dtNeg = cabVO.asTimestamp("DTNEG");
}
```

### Consultar por Critério (Finder / Where):
```java
JapeWrapper dao = JapeFactory.dao(DynamicEntityNames.ITEM_NOTA);
Collection<DynamicVO> itens = dao.find("NUNOTA = ? AND QTDNEG > ?", nuNota, BigDecimal.ZERO);
for (DynamicVO item : itens) {
    BigDecimal codProd = item.asBigDecimal("CODPROD");
}
```

### Atualizar Registro (Dirty-Check / Fluent):
```java
dao.prepareToUpdate(cabVO)
   .set("OBSERVACAO", "Processado via integração")
   .update();
```

### Excluir Registro:
```java
dao.delete(new Object[]{ nuNota });
```

---

## 3. NativeSql (Uso Criterioso)

Use `NativeSql` apenas quando o JAPE não atender (queries analíticas pesadas, joins complexos com agregações):

```java
NativeSql sql = null;
ResultSet rs = null;
JdbcWrapper jdbc = null;
try {
    EntityFacade dwf = EntityFacadeFactory.getDWFFacade();
    jdbc = dwf.getJdbcWrapper();
    sql = new NativeSql(jdbc);
    
    // Parâmetros nomeados com :param (prevenção contra SQL Injection)
    sql.appendSql("SELECT NUNOTA, VLRNOTA FROM TGFCAB WHERE CODPARC = :CODPARC AND STATUSNOTA = 'L'");
    sql.setNamedParameter("CODPARC", codParc);
    
    rs = sql.executeQuery();
    while (rs.next()) {
        BigDecimal nuNota = rs.getBigDecimal("NUNOTA");
        BigDecimal vlrNota = rs.getBigDecimal("VLRNOTA");
    }
} finally {
    NativeSql.releaseResources(sql, rs);
}
```

## Regras de Ouro de Performance JAPE
- Nunca execute queries JAPE ou `NativeSql` dentro de loops iterativos (problema N+1). Agrupe ou busque coleções.
- Nunca feche conexões JDBC manuais que foram abertas pelo JAPE/DWFFacade; use sempre `releaseResources`.
- Respeite as propriedades de sessão do Sankhya: `JapeSession.putProperty("usuario_logado", codUsu)`.
