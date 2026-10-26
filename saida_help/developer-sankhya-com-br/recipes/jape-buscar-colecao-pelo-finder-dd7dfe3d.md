---
id: "https://developer.sankhya.com.br/recipes/jape-buscar-coleção-pelo-finder"
titulo: "Jape - Buscar Coleção pelo Finder"
url: "https://developer.sankhya.com.br/recipes/jape-buscar-coleção-pelo-finder"
atualizado_em: "2025-11-10T23:38:33.000Z"
---

# Jape - Buscar Coleção pelo Finder

```java Java
public void buscaEmpPorCep(ServiceContext ctx) throws MGEModelException {
    SessionHandle hnd = null;
    try {
      hnd = JapeSession.open();
      EntityFacade dwfFacade = EntityFacadeFactory.getDWFFacade();

      FinderWrapper finder = new FinderWrapper(DynamicEntityNames.EMPRESA, "this.CEP = ?", new Object[] { "38400102" });
      finder.setOrderBy("CODEMP");
      finder.setMaxResults(-1);
      Collection<DynamicVO> saldosVO = dwfFacade.findByDynamicFinderAsVO(finder);

      for (DynamicVO dynamicVO : saldosVO) {
        System.out.println(dynamicVO.asBigDecimal("CODEMP"));
      }
    } catch (Exception e) {
      MGEModelException.throwMe(e);
    } finally {
      JapeSession.close(hnd);
    }
}
```

```json Response Example
{"success":true}
```

# Inicio

<!-- java@1 -->

Inicio do serviço

# Instanciamento

<!-- java@2 -->

o SessionHandle é instanciado, que será o objeto de habilitação de acesso ao banco de dados.

# Try catch finally- Prevenção de erros

<!-- java@3-19 -->

Por padrão. é criado um try para garantir que a sessão será fechada, prevenindo erros.

# Abertura da Sessão

<!-- java@4 -->

Abertura da sessão que vai possibilitar a execução dos (SELECT)

# Instanciamento do Objeto

<!-- java@5 -->

É feito o instanciamento do objeto no framework, que vai dar acesso as entidades da Sankhya

# Criação da regra de SELECT

<!-- java@7 -->

Criação do finder que será a regra de SELECT, primeiro argumento deve ser o nome da entidade (EMPRESA);  pode ser usada string ou DynamicEntityNames, que mapeia as entidades mais utilizadas.   

SELECT montado com o WHERE  (CEP) igual ao argumento informado (38400102)

# Regra de ordenação

<!-- java@8 -->

Regra de ordenação (linha opcional)

# Retirando limite de resultados

<!-- java@9 -->

Por padrão, o MaxResults é 500. Para retirar este limite, alteramos para -1

# Pesquisa

<!-- java@10 -->

Pesquisa é efetuada no (dwfFacade), é retornado um Collection<DynamicVO>, seria um registro que o select foi encontrado.

# Coleta de dados

<!-- java@12-14 -->

É executado o for, preenchendo a array saldosVO, em seguida os valores são acessados. Nesta etapa é possivel ler qualquer coluna (CODEEMP) no DynamicVO

# Finalização da sessão

<!-- java@17 -->

A sessão é finalizada.

# Fim da busca

<!-- java@18 -->

Fim da busca
