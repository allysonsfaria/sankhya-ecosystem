# Framework Frontend Legado (sankhya-js / AngularJS 1.x)

O framework `sankhya-js` suporta a interface legada HTML5 do ERP Sankhya OM, baseado em AngularJS 1.x e componentes proprietários (`snk-*`).

---

## 1. Comunicação com Backend via ServiceProxy e FluidBuilder

Nas telas clássicas em HTML/JSP do Sankhya, as chamadas para o backend utilizam o serviço angular `ServiceProxy`:

```javascript
angular.module('meuModulo').controller('MinhaTelaController', function($scope, ServiceProxy) {

    $scope.carregarDados = function(codParc) {
        ServiceProxy.callService('CRUDServiceProvider.loadRecords', {
            dataSet: {
                rootEntity: 'Parceiro',
                criteria: {
                    expression: 'this.CODPARC = ' + codParc
                },
                entity: {
                    fieldset: { list: 'CODPARC,NOMEPARC,CGC_CPF' }
                }
            }
        }).then(function(response) {
            $scope.parceiro = response.responseBody.entities.entity;
        }).catch(function(erro) {
            alert('Falha ao consultar: ' + erro.statusMessage);
        });
    };
});
```

---

## 2. Invocação Fluente com FluidBuilder

```javascript
ServiceProxy.call('comercial.faturamento.cancelarNota')
    .setParam('nuNota', 102030)
    .setParam('motivo', 'Cancelado pelo usuário na tela')
    .then(function(result) {
        // sucesso
    });
```

---

## 3. Diretrizes de Manutenção em Código sankhya-js
- **Não introduzir novas telas em sankhya-js** para novos desenvolvimentos; prefira o Addon Studio 2.0 e o Sankhya Design System (`ez-*`).
- Em manutenção de telas existentes, preserve as injeções de `$scope`, `MetadataProvider` e `SkI18nService`.
