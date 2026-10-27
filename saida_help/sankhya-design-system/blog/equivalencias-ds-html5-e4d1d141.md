---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5"
titulo: "Equivalências DS/HTML5"
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5"
trilha: "Blog > Equivalencias Ds Html5"
---

# Equivalências DS/HTML5

23 de agosto de 2024 · 4 min para ler

![André Luiz Barquet Moreira](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/AndreMoreira.jpg)

André Luiz Barquet Moreira

Developer

## Introdução

Este artigo tem como objetivo documentar a relação/equivalência entre componentes e métodos utilitários implementados no novo
design system relacionados com os já existentes no HTML5 visando facilitar o entendimento e utilização dos componentes ou
métodos à serem utilizados durante a migração ou implementação de alguma nova tela ou feature.

### Lista de equivalências

| HTML5 Design System| [sk-dataset](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#dataSet--dataUnit) [snk-dataunit](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#dataSet--dataUnit)| [sk-field](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skField--getFieldMap) [getFieldMap do IDataUnitInterceptor](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skField--getFieldMap)| [sk-dynaform](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skDynaform--snkCrud) [snk-crud](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skDynaform--snkCrud)| [sk-left-top-bar](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skLeftTopBar--taskbar) [SnkCustomSlotElements, customButtons e taskbarManager](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skLeftTopBar--taskbar)| [sk-other-options-loader](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skOtherOptionsLoader--snkTaskbarActionsList) [snk-taskbar.actionsList](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skOtherOptionsLoader--snkTaskbarActionsList)| [IDynaformInterceptor.prototype.interceptFieldMetadata](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#interceptFieldMetadata--duMetaData) [Alterar metadados diretamente no dataunit](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#interceptFieldMetadata--duMetaData)| [IFormInterceptor.prototype.buildFieldContainer](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#buildFieldContainer--onFormItemsReady) [SnkForm.onFormItemsReady](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#buildFieldContainer--onFormItemsReady)| [sk-dynamic-filter-panel](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skDynamicFilterPanel--snkFilterBar) [snk-filter-bar](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skDynamicFilterPanel--snkFilterBar)| [sk-configurable-form, sk-dynaform](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skDynaform--snkSimpleCrud) [snk-simple-crud](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skDynaform--snkSimpleCrud)| [sk-form](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skForm--snkForm) [snk-form](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skForm--snkForm)| [sk-grid](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skGrid--skGrid) [snk-grid](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skGrid--skGrid)| [sk-attach, sk-entity-attach](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skAttach--skAttach) [snk-attach](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#skAttach--skAttach)| [MGEParameters](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#mgeParameters--snkApplication) [snk-application](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#mgeParameters--snkApplication)| [SkApplicationInstance.hasAuthorization](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#hasAuthorization--snkApplication) [SnkApplication](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#hasAuthorization--snkApplication)| [ServiceProxy.addClientEvent](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#addClientEvent--addClientEvent) [SnkApplication.addClientEvent](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#addClientEvent--addClientEvent)| [DefaultSankhyaApplicationController.loadByPK](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#loadByPK--loadByPK) [SnkApplication.loadByPK](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#loadByPK--loadByPK)| [SanPopup](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#sanPopup--ezPopup) [SnkApplication.showPopUp ou ez-popup](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#sanPopup--ezPopup)| [dataset.addObserver](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#addObserver--addInterceptor) [Dataunit.addInterceptor e subscribe](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#addObserver--addInterceptor)| [dataset.crudListener](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#crudListener--IDataUnitCrudListener) [IDataUnitCrudListener](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#crudListener--IDataUnitCrudListener)| [dataset.metadataInterceptor](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#metadataInterceptor--IDataUnitInterceptor) [IDataUnitInterceptor](https://gilded-nasturtium-6b64dd.netlify.app/blog/equivalencias-ds-html5#metadataInterceptor--IDataUnitInterceptor) | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Exemplos de uso

**sk-dataset / snk-dataunit**

```
    // HTML5:
    // utilização "sk-dataset"
    <sk-dataset
        sk-dataset-created="ctrl.onDatasetCreated(dataset)"
        parent-dataset="ctrl.dsAgendamentoProcessamento"
        entity-name="HistoricoProcessamentoXMLAG"
        order-by="DHEXEC DESC"
    >
        <sk-field pattern="*"></sk-field>
    </sk-dataset>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // utilização "SnkDataUnit"
    <SnkDataUnit
        className="ez-size-height--full ez-box__container ez-flex--column"
        entityName="LogRegistrosMDe"
        dataUnitName="LogRegistrosMDe"
        key="duLogRegistrosMDe"
    >
```

**Para mais detalhes sobre a utilização do Data Unit:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-data-unit/)

**sk-field / getFieldMap do IDataUnitInterceptor**

```
    // HTML5:
    // utilização "sk-field", informa no "pattern" o campo da tabela relacionada,
    // e no "path" a entidade da tabela relacionada
    <sk-dataset entity-name="CabecalhoNota" sk-dataset-created="ctrl.onDatasetCreatedPedidosGerados(dataset)">
        <sk-field pattern="CTE,NFE,NFSE,CODMODDOC,TIPMOV,ARMTIPAPU,VALIDAAGRUPMIN" path="TipoOperacao"></sk-field>
        <sk-field pattern="TIPOFATUR" path="Parceiro"></sk-field>
        <sk-field pattern="NOMEFANTASIA,CGC"  path="Empresa"></sk-field>
    </sk-dataset>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // Criar uma classe com o final "DataUnitInterceptor", dentro da pasta
    // {projeto-bff}/src/br/com/sankhya/mgecom/dataUnit/interceptors/
    // implementando a "IDataUnitInterceptor", (passando a entidade e o resourceId
    // utilizados no DataUnit), sobrescrevendo o método "getFieldMap()", adicionando
    // new DataUnitFieldMap para cada tabela relacionada, informando os campos separando
    // por virgula. Obs: SEM ESPACO entre as vírgulas
    package br.com.sankhya.mgecom.dataUnit.interceptors;

    import br.com.sankhya.modelcore.dataunit.DataUnitDataType;
    import br.com.sankhya.modelcore.dataunit.DataUnitUserInterface;
    import java.util.ArrayList;
    import java.util.List;
    import br.com.sankhya.modelcore.dataunit.DataUnitFieldMap;
    import br.com.sankhya.modelcore.dataunit.annotations.DataUnitInterceptor;
    import br.com.sankhya.modelcore.dataunit.interceptor.IDataUnitInterceptor;

    @DataUnitInterceptor(entity = "CabecalhoNota", resourceId = "br.com.sankhya.mgecom.mov.selecaodedocumento")
    public class CabecalhoNotaSelecaoPortalDataUnitInterceptor implements IDataUnitInterceptor {

        @Override
        public List<DataUnitFieldMap> getFieldMap() {
            List<DataUnitFieldMap> mappedFields = new ArrayList<DataUnitFieldMap>();
            mappedFields.add(new DataUnitFieldMap("TipoOperacao", "CTE,NFE,NFSE,CODMODDOC,TIPMOV,ARMTIPAPU,VALIDAAGRUPMIN"));
            mappedFields.add(new DataUnitFieldMap("Parceiro", "TIPOFATUR"));
            mappedFields.add(new DataUnitFieldMap("Empresa", "NOMEFANTASIA,CGC"));
            return mappedFields;
        }
    }
```

**sk-dynaform / snk-crud**

```
    // HTML5:
    // utilização "sk-dynaform"
    <sk-dynaform
        sk-entity-name="PreAcordoVerba"
        sk-resource-id="br.com.sankhya.Rotinas.PreAcordoVerba"
    >
    </sk-dynaform>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // utilização "SnkCrud"
    // Obs: O "SnkCrud" Precisa SEMPRE ser filho/estar dentro de um "SnkDataUnit"
    <SnkDataUnit
        resourceID="br.com.sankhya.Rotinas.PreAcordoVerba"
        entityName="PreAcordoVerba"
        dataUnitName="nome_data_unit"
        key="chave_data_unit"
    >
        <SnkCrud />
    </SnkDataUnit>
```

**Para mais detalhes sobre a utilização do SnkCrud:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-crud/)

**sk-left-top-bar / SnkCustomSlotElements, customButtons e taskbarManager**

```
    // HTML5:
    // utilização "sk-left-top-bar", passando como filho, os componentes a serem renderizados na taskbar
    <sk-dynaform
        sk-id="ctrl.dynaformAgendamentoTarefa"
        sk-entity-name="AgendamentoTarefa"
        sk-on-dynaform-loaded="ctrl.onDynaformLoaded(dynaform,dataset)"
        sk-custom-tabs-loader="ctrl.customTabsLoader(entityName)"
        sk-form-interceptor="ctrl"
    >
        <dynaform-agendamento-tarefa>
            <sk-left-top-bar>
                <button type="button" ng-click="ctrl.forcarEnvio()" ng-show="true">
                    <span>Novo botao</span>
                </button>
            </sk-left-top-bar>
        </dynaform-agendamento-tarefa>
    </sk-dynaform>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // utilização "SnkCustomSlotElements", por exemplo dentro de um SnkGrid
    <SnkDataUnit entityName="AgendamentoTarefa" dataUnitName="nome_data_unit">
        <SnkGrid>
            <SnkCustomSlotElements slotName="GRID_HEADER_CUSTOM_ELEMENTS">
                <EzButton
                    label="Novo botao
                    onClick={forcarEnvio}
                />
            </SnkCustomSlotElements>
        </SnkGrid>
    </SnkDataUnit>

    // OU

    // utilização "taskbarManager e customButtons",
    function buildTaskBarManager(): TaskbarManager {
        return {
            getButtons: (taskBarId, dataState, currentButtons) => {
                return [...currentButtons, "CUSTOM_BUTTON_ID"];
            }
        };
    }

    <SnkDataUnit entityName="AgendamentoTarefa" dataUnitName="nome_data_unit">
        <SnkGrid taskbarManager={buildTaskbarManager()}>
            <div slot="GRID_HEADER_CUSTOM_ELEMENTS" className="ez-flex ez-margin-left--medium">
                <div id="CUSTOM_BUTTON_ID" className="ez-flex">
                  <EzButton
                    label="Novo botao
                    onClick={forcarEnvio}
                  />
                </div>
            </div>
        </SnkGrid>
    </SnkDataUnit>
```

**Obs: se necessário utilizar a Taskbar separadamente, utilizar o SnkTaskbar:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-taskbar/)

**sk-other-options-loader / snk-taskbar.actionsList**

```
    // HTML5:
    // O "sk-other-options-loader" é uma prop do sk-dynaform, é passado para o mesmo uma lista
    // com as opções que serão mostradas no menu de "outras opções" ou uma função que retorne e lista

    function otherOptionsLoader() {
        var options = [
            { label: "Opção 1", action: () => { console.log("executarOpcao1") } },
            { label: "Opção 2", action: () => { console.log("executarOpcao2") } }
        ];
        return options;
    }

    <sk-dynaform sk-pk-listener id="dynaformListaServico" sk-entity-name="ListaServicoSintegra"
        sk-other-options-loader="ctrl.otherOptionsLoader()"
        sk-on-dynaform-loaded="ctrl.onDynaformLoaded(dynaform, dataset)" sk-hierarchy sk-can-back-to-old-layout="true"
        sk-datagrid-interceptor="ctrl"
        sk-form-interceptor="ctrl"
        flex>
    </sk-dynaform>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // O "actionsList" é uma prop do SnkTaskbar que precisa de uma lista
    // com as opções que serão mostradas no menu de "outras opções" ou uma função que retorne e lista
    const actionsList = [{
        label: "Opção 1",
        value: "OPPEN_APP: br.com.sankhya.mge.nome_da_tela_1",
        iconName: "settings-inverted"
    }, {
        label: "Opção 2",
        value: "OPPEN_APP: br.com.sankhya.mge.nome_da_tela_2",
        iconName: "business-center"
    }];

    <SnkDataUnit ref={snkDataUnit} entityName="ListaServicoSintegra">
        <SnkTaskbar
            actionsList={actionsList}>
        </SnkTaskbar>
    </SnkDataUnit>

    // Vários componentes utilizam o SnkTaskbar por baixo dos panos, eles também tem a mesma prop "actionsList"
    // Exemplo de utilização "actionsList" dentro de um SnkGrid
    // É passado para o mesmo uma lista com as opções que serão mostradas no menu de "outras opções"
    // ou uma função que retorne e lista

    function otherOptions() {
        const options = [{
            label: "Opção 1",
            value: "OPPEN_APP: br.com.sankhya.mge.nome_da_tela_1",
            iconName: "settings-inverted"
        }, {
            label: "Opção 2",
            value: "OPPEN_APP: br.com.sankhya.mge.nome_da_tela_2",
            iconName: "business-center"
        }];
        return options;
    }

    <SnkDataUnit entityName="ListaServicoSintegra" dataUnitName="nome_data_unit">
        <SnkGrid actionsList={otherOptions} />
    </SnkDataUnit>
```

**Mais detalhes sobre a lista de ações:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-taskbar/#lista-de-ações)

**IDynaformInterceptor.prototype.interceptFieldMetadata / Alterar metadados diretamente no dataunit**

```
    // HTML5:
    self.interceptFieldMetadata = interceptFieldMetadata;

    function interceptFieldMetadata(fieldMetadata, dataset, dynaform) {
        if (fieldMetadata.fieldName === "TESTE) {
            fieldMetadata.visible = false;
        }
    }

    <sk-dataset entity-name="SerieProduto" sk-standalone>
        <sk-field pattern="*"></sk-field>
    </sk-dataset>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    import { ApplicationContext } from "@sankhyalabs/core";

    function initDataUnit(){
        const snkApp = ApplicationContext.getContextValue("__SNK__APPLICATION__");
        const dataUnit = await snkApp.getDataUnit("SerieProduto", "SerieProduto_");
        let metadata = dataUnit.metadata;

        metadata.fields = metadata.fields.map((field) => {
            if (field.name === "TESTE") {
                field.visible = false;
            }

            return field;
        })

        dataUnit.metadata = metadata;
        return dataUnit;
    }
```

**IFormInterceptor.prototype.buildFieldContainer / SnkForm.onFormItemsReady**

```
    // HTML5:
    self.buildFieldContainer = buildFieldContainer;

    function buildFieldContainer(fieldName, dataset, fieldElem, scope){
        if (fieldName == "PRAZOPARCELAS"){
            scope.dsFinanceiroTipTit = dataset;
            var hBoxElem = AngularUtil.createDirective('sk-hbox', {}, scope);

            var _lblAVista = AngularUtil.createDirective('span', {
                'sk-i18n':'Comercial.CentralNotas.lblAvista',
                'sk-color':'red',
                'style': 'margin-top: 5px'
            }, scope);

            hBoxElem.append(_lblAVista);
            return hBoxElem;
        }
    }

    <sk-dataset entity-name="SerieProduto" sk-standalone>
        <sk-field pattern="*"></sk-field>
    </sk-dataset>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    function onFormItemsReady(elements) {
        const formItem = elements.get('PRAZOPARCELAS');
        const launchButton = document.createElement('ez-badge');

        launchButton.size = 'medium';
        launchButton.iconLeft = 'alert-circle-inverted';
        launchButton.title = i18n("LancamentoPortal.ParcelarVariosTipTit.aVista");
        launchButton.className = 'ez-margin-vertical--auto ez-padding-bottom--large ez-badge--warning-subtle';
        badgeControllerRef.current = {
            add: () => formItem?.addRightElement(launchButton),
            remove: () => formItem?.removeRightElement(),
        }
    }

    <SnkSimpleCrud onFormItemsReady={({ detail }) => onFormItemsReady(detail.items)} />
```

**sk-dynamic-filter-panel / snk-filter-bar**

```
    // HTML5:
    <sk-dynamic-filter-panel>
	    <default-group label="Financeiro.MovimentacaoFinanceira.lblFiltrosRapidos" icon="{{ctrl.filtrosIconFilter}}">
	        <sk-simple-form sk-columns="2">
	            <sk-simple-item sk-label="Financeiro.MovimentacaoFinanceira.headerReceitas">
	                <sk-switch sk-value="ctrl.chkReceita" sk-enabled="ctrl.chkReceitaEnabled" sk-change="ctrl.validaFiltroRec(ctrl.chkReceita, ctrl.chkDespesa)">
	            </sk-simple-item>
	            <sk-simple-item sk-label="Financeiro.MovimentacaoFinanceira.headerReal">
	                <sk-switch sk-value="ctrl.chkReal" sk-change="ctrl.validaFiltroReal(ctrl.chkReal, ctrl.chkProvisao)">
	            </sk-simple-item>
	        </sk-simple-form>
	        <sk-simple-form sk-columns="1">
	            <sk-simple-item sk-label="Financeiro.MovimentacaoFinanceira.headerDataVencimento">
	                <sk-date-period sk-value="ctrl.periodoVencimento"></sk-date-period>
	            </sk-simple-item>
	            <sk-simple-item sk-label="Financeiro.MovimentacaoFinanceira.headerDataNegociacao">
	                <sk-date-period sk-value="ctrl.periodoNegociacao"></sk-date-period>
	            </sk-simple-item>
	        </sk-simple-form>
	    </default-group>
    </sk-dynamic-filter-panel>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // Exemplo de implementação usando separadamente
    <SnkDataUnit
        entityName="MovimentoBancario"
        dataUnitName="principal"
        key="duPrincipal"
    >
        <SnkFilterBar configName="MovimentoBancario" />
    </SnkDataUnit>

    // Como o "SnkFilterBar" é utilizado por outros componentes por baixo dos panos
    // como SnkCrud, SnkGrid, etc. temos também o seguinte exemplo de utilização:

    <SnkDataUnit
      dataUnit={cabecalhoNotaDU}
      onMessagesBuilderUpdated={handlerUpdateMessageBuilder}
    >
        <SnkGrid
          filterBarTitle"Titulo"
          resourceID="br.com.sankhya.resourceIdTeste"
          configName="CabecalhoNota"
        />
    </SnkDataUnit>

    // Obs: para utilizar nos outros componentes é preciso criar um json com exatamente o
    // nome do resourceID informado no componente, no caso "br.com.sankhya.resourceIdTeste.json"
    // dentro da pasta {projeto-bff}/webapp/WEBINF/resources/filter-config como o exemplo a seguir:
    {
        "items": [
            {
                "id": "DTOCORRENCIA",
                "visible": true,
                "type": "PERIOD",
                "label": "Período",
                "detailTitle": "Informe a data ou período",
                "detailModal": "Período",
                "filterType": "QUICK_FILTER",
                "props": {
                    "expression": {
                        "fullfill": "onlydate(this.DTOCORRENCIA) >= :DTOCORRENCIA.START AND onlydate(this.DTOCORRENCIA) <= :DTOCORRENCIA.END",
                        "onlystart": "onlydate(this.DTOCORRENCIA) >= :DTOCORRENCIA",
                        "onlyend": "onlydate(this.DTOCORRENCIA) <= :DTOCORRENCIA"
                    }
                }
            }
        ]
    }
```

**Para mais detalhes sobre a utilização do SnkFilterbar:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-filter-bar/)

**sk-configurable-form, sk-dynaform / snk-simple-crud**

```
    // HTML5:
    // Utilização "sk-configurable-form"
    <sk-configurable-form
    	sk-uid="{{skUid}}"
    	sk-in-line="true"
    	sk-dataset="ctrl.dsPreAcordoVerba"
    	sk-form-interceptor="ctrl"
    	sk-on-created="ctrl.onConfigurableFormCreated(formApi)"
    	layout-padding>
    </sk-configurable-form>

    // Utilização "<sk-dynaform"
    <sk-dynaform
        sk-entity-name="PreAcordoVerba"
        sk-resource-id="br.com.sankhya.Rotinas.PreAcordoVerba">
    </sk-dynaform>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // Utilização "SnkSimpleCrud" com instancia do DataUnit
    <SnkSimpleCrud
        configName="preAcordoVerba"
        dataUnit={new DataUnit("PreAcordoVerba")}
    />

    // OU
    // Utilização "SnkSimpleCrud" com o nome da entidade
    <SnkSimpleCrud
        configName="preAcordoVerba"
        entityName="PreAcordoVerba"
    />
```

**Para mais detalhes sobre a utilização do SnkSimpleCrud:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-crud/)

**sk-form / snk-form**

```
    // HTML5:
    // Utilização "sk-form"
    <sk-form
        sk-dataset="ctrl._ds"
        sk-columns="1"
        sk-inline="true"
        class="compact-components"
        sk-only-custom>
    </sk-form>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // Utilização "SnkForm"
    // Obs: Para que funcione corretamento o SnkForm tem que SEMPRE
    // estar dentro/ser filho de um componente SnkDataUnit
    <SnkDataUnit entityName="MovimentoBancario">
        <SnkForm configName="MovimentoBancario" />
    </SnkDataUnit>
```

**Para mais detalhes sobre a utilização do SnkForm:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-form/)

**sk-grid / snk-grid**

```
    // HTML5:
    // Utilização "sk-grid"
    <sk-datagrid
        sk-uid="gridNotaDestino"
        sk-dataset="ctrl.ds.destino"
        sk-on-dbl-click="ctrl.openDocumento('destino')"
        sk-grid-config="{{ ::ctrl.gridConfig.destino }}"
        sk-disable-tour="true"
        sk-editable="false"
        sk-width="100%"
        sk-height="100%"
    >
    </sk-datagrid>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // Utilização "SnkGrid"
    // Obs: Para que funcione corretamento o SnkGrid tem que SEMPRE
    // estar dentro/ser filho de um componente SnkDataUnit
    <SnkDataUnit
        className="ez-size-width--full"
        entityName="CabecalhoNota"
        dataUnitName="DataUnitDestino"
    >
        <SnkGrid
            configName="DestinoRelacaoDocumento"
            presentationMode={"secondary" as PresentationMode}
            taskbarManager={buildTaskBarManager(nuNota)}
            canEdit={false}
        >
    </SnkDataUnit>
```

**Para mais detalhes sobre a utilização do SnkGrid:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-grid/)

**sk-attach, sk-entity-attach / snk-attach**

```
    // HTML5:
    // utilização "sk-attach"
    <sk-attach
        id="attach"
        sk-tipo="N"
        flex="grow"
        layout>
    </sk-attach>

    // OU

     <sk-entity-attach
        sk-entity-name="Custo"
        sk-resource-id="{{ctrl.resourceIDAnexoCustos}}"
        sk-dataset="ctrl.dsCusto"
        sk-margin-right="5px">
    </sk-entity-attach>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // utilização "SnkAttach"
    // Obs: é necessário informar o "messagesBuilder={snkApp.messagesBuilder}" para que funcione corretamente
    import { ApplicationContext } from "@sankhyalabs/core";

    const snkApp = ApplicationContext.getContextValue("__SNK__APPLICATION__");

    <SnkAttach
        className="ez-flex-item--auto"
        registerKey="1_2
        fetcherType="Attach"
        messagesBuilder={snkApp.messagesBuilder}
    />

    // OU

    <SnkAttach
        className="ez-flex-item--auto"
        registerKey="1_2
        entityName="Custo"
        messagesBuilder={snkApp.messagesBuilder}
    />
```

**Para mais detalhes sobre a utilização do SnkAttach:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-attach/)

**MGEParameters / snk-application**

```
    // HTML5:
    // utilização "MGEParameters"
    function buscarParametros() {
        var paramHabilitarFormasRepRed = MGEParameters.asBoolean('habilitar.formas.alternativas.repasse.icms');
        var distribuidorCombustivel = MGEParameters.asInteger('fin.movimentacao.financeira.max.dias.filtro');
    }

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // utilização "SnkApplication"
    const snkApplicationRef = useRef(null);

    async function buscarParametros() {
        const paramHabilitarFormasRepRed = snkApplicationRef.current.getBooleanParam('habilitar.formas.alternativas.repasse.icms');
        const distribuidorCombustivel = snkApplicationRef.current.getIntParam('fin.movimentacao.financeira.max.dias.filtro');
    }

    <SnkApplication ref={snkApplicationRef}>
        {......}
    </SnkApplication>

    // OU
    import { ApplicationContext } from "@sankhyalabs/core";

    async function buscarParametros() {
        const snkApp = ApplicationContext.getContextValue("__SNK__APPLICATION__");
        const paramHabilitarFormasRepRed = await snkApp.getBooleanParam('habilitar.formas.alternativas.repasse.icms');
        const distribuidorCombustivel = await snkApp.getIntParam('fin.movimentacao.financeira.max.dias.filtro');
    }
```

**Para mais detalhes sobre a utilização do SnkApplication:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-application/)

**SkApplicationInstance.hasAuthorization / SnkApplication**

```
    // HTML5:
    // utilização "MGEParameters"
    function buscarAcessos() {
        var podeInserir = SkApplicationInstance.hasAuthorization("I");
        var podeAtualizar = SkApplicationInstance.hasAuthorization("A");
        var podeRemover = SkApplicationInstance.hasAuthorization("E");
    }

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // utilização "SnkApplication"
    import { ApplicationContext } from "@sankhyalabs/core";

    async function buscarParametros() {
        const snkApp = ApplicationContext.getContextValue("__SNK__APPLICATION__");
        const podeInserir = await snkApp.hasAccess("I", /* se necessario passar o resourceId da tela como segundo argumento */);
        const podeAtualizar = await snkApp.hasAccess("A", /* se necessario passar o resourceId da tela como segundo argumento */);
        const podeAtualizar = await snkApp.hasAccess("E", /* se necessario passar o resourceId da tela como segundo argumento */);
    }
```

**Para mais detalhes sobre a utilização do SnkApplication:**
[Ver documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-application/)

**ServiceProxy.addClientEvent / SnkApplication.addClientEvent**

```
    // HTML5:
    // utilização "MGEParameters"
    function adicionarClientEvents() {
        ServiceProxy.addClientEvent("br.com.sankhya.recebimento.com.cartao.antes.aprovacao.sefaz", (eventContent, serviceRecaller) => {});
        ServiceProxy.addClientEvent("br.com.sankhya.aprovar.nota.apos.recebimento.cartao", (eventContent, serviceRecaller) => {});
    }

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // utilização "SnkApplication.addClientEvent"
    import { ApplicationContext } from "@sankhyalabs/core";

    async function adicionarClientEvents() {
        const snkApp = ApplicationContext.getContextValue("__SNK__APPLICATION__");
        snkApp.addClientEvent("br.com.sankhya.recebimento.com.cartao.antes.aprovacao.sefaz", (clientEvent, serviceRecaller) => {});
        snkApp.addClientEvent("br.com.sankhya.aprovar.nota.apos.recebimento.cartao", (clientEvent, serviceRecaller) => {});
    }
```

**DefaultSankhyaApplicationController.loadByPK / SnkApplication.loadByPK**

```
    // HTML5:
    // utilização "MGEParameters"
    function adicionarClientEvents() {
        DefaultSankhyaApplicationController.loadByPK = (param: GenericObject) => {
            console.log(param.pk)
        };
    }

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // utilização "SnkApplication.loadByPK"
    import { ApplicationContext } from "@sankhyalabs/core";

    async function adicionarClientEvents() {
        const snkApp = ApplicationContext.getContextValue("__SNK__APPLICATION__");

        snkApp.loadByPK = (param: GenericObject) => {
            console.log(param.pk)
        };
    }
```

**SanPopup / SnkApplication.showPopUp ou ez-popup**

```
    // HTML5:
    // utilização "SanPopup.open"
    function mostrarPopup() {
        SanPopup.open({
            title: "Titulo",
            templateUrl: 'html5/BaixaTitulosDespesasCheque/popup/BaixaTitulosDespChequesPopUp.tpl.html',
            controller: 'BaixaTituloDespController',
            controllerAs: 'ctrl',
            size: 360,
            height: 400,
            bodyPadding: false,
            showBtnOk: true,
            showBtnCancel: true,
            showBtnNo: false,
            okBtnLabel: "Confirmar",
            resolve: {
                dataValue: {
                    totalChque: 123,
                    vlrDiferenca: 123,
                }
            }
        }).result.then(function (result) {
            self.dataSetFinanceiro.refresh();
            self.dataSetFinanceiroDesp.refresh();
        });
    }

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // utilização "EzPopup" (forma mais utilizada e mais recomendada)
    const [showPopUp, setShowPopUp] = useState<boolean>(true);

    <EzPopup
        size="medium"
        heightMode="auto"
        opened={showPopUp}
        onEzClosePopup={() => setShowPopUp(false)}
        ezTitle="Titulo"
    >
        <div className="ez-flex ez-flex--column">
            <p>Conteúdo popup</p>
        </div>
    </EzPopup>

    // utilização "SnkApplication.showPopup" (forma menos utilizada)
    import { ApplicationContext } from "@sankhyalabs/core";

    function mostrarPopup() {
        const snkApp = ApplicationContext.getContextValue("__SNK__APPLICATION__");

        const popupElement = document.createElement("ez-modal-container");
        popupElement.modalTitle = "Titulo";
        popupElement.modalSubTitle = "Sub Titulo";
        popupElement.cancelButtonLabel = "Cancelar";
        popupElement.okButtonLabel = "Confirmar";
        popupElement.addEventListener("ezModalAction", (action) => {
            console.log("Finalizou")
        });

        const dataValue = { totalChque: 123, vlrDiferenca: 123 }
        ReactDOM.render(<ComponenteARenderizar dataValue={dataValue} />,  popupElement)
        snkApp.showPopUp(popupElement, "auto");
    }
```

**dataset.addObserver / Dataunit.addInterceptor e subscribe**

```
    // HTML5:
    // utilização "dataSet.addObserver"
    var observer = new IDataSetObserver();
    observer.insertionModeActivated = function() {
        if (self.dsCusto.isCopyingRecord()) {
            console.log("Copiou o registro!")
        }
    };

    observer.editionCanceled = function() {
        console.log("edição cancelada!")
    };

    self.dsCusto.addObserver(observer);

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // Podem ser usados tanto o "subscribe" quanto o "addInterceptor" as
    // diferenças entre eles são no ciclo de vida, o "addInterceptor" é
    // executado antes de executar uma ação para intercepta-la manipulando
    // algo antes de enviar para a requisição, retornando a "action"

    // utilização "dataUnit.subscribe"
    import { ApplicationContext } from "@sankhyalabs/core";

    function onDataUnitEvent(action: DataUnitAction) {
        if (action?.type === Action.RECORDS_COPIED) {
            console.log("Copiou o registro!");
        }

        if (action?.type === Action.EDITION_CANCELED) {
            console.log("Inserção cancelada!");
        }
    }

    async function initDataUnit() {
        const snkApp = ApplicationContext.getContextValue("__SNK__APPLICATION__");
        const dataUnit = await snkApp.getDataUnit("CabecalhoNota", "CabecalhoNota_id");
        dataUnit.subscribe(onDataUnitEvent);
    }

    // utilização "dataUnit.addInterceptor"
    import { ApplicationContext } from "@sankhyalabs/core";

    const dataUnitInterceptor = {
        interceptAction: (action: DataUnitAction) => {
            if(action?.type === Action.RECORDS_COPIED){
                console.log(Irá copiar o registro!");
            }

            if (action.type === Action.EDITION_CANCELED) {
                // Caso queira manipular algo, exemplo abaixo:
                // action.payload.fields = action.payload.fields.map((field: any) => {
                //     return { ...field, visible: true};
                // });

                console.log(Irá cancelar a edição!");
            }

            return action;
        }
    }

    async function initDataUnit() {
        const snkApp = ApplicationContext.getContextValue("__SNK__APPLICATION__")
        const dataUnit = await snkApp.getDataUnit("CabecalhoNota", "CabecalhoNota_id");
        dataUnit.addInterceptor(dataUnitInterceptor);
    }
```

**dataset.crudListener / IDataUnitCrudListener**

```
    // HTML5:
    // Informa na string o caminho da classe java onde está o interceptor
    function onDatasetCreated(dataset) {
        dataset.setCrudListener("br.com.sankhya.modelcore.comercial.ItemNotaCrudListener");
    }

    <sk-dataset entity-name="ItemNota" sk-dataset-created="ctrl.onDatasetCreated(dataset)" sk-standalone>
        <sk-field pattern="CODPROD, REFERENCIA, REFFORN, CONTROLE, QTDNEG, CODVOL" ></sk-field>
    </sk-dataset>

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // Para utilizar no DS, é necessário criar uma classe com o final "IDataUnitCrudListener",
    // dentro da pasta "{projeto-bff}/src/br/com/sankhya/mgecom/dataUnit/listener/", implementando
    // a "IDataUnitCrudListener", sobrescrevendo os métodos que forem necessários:
    // (passando a entidade e o resourceId utilizados no DataUnit do SnkCrud)
    package br.com.sankhya.mgecom.dataUnit.listeners;

    import java.util.Collection;
    import java.util.logging.Level;
    import java.util.logging.Logger;

    import br.com.sankhya.jape.util.FinderWrapper;
    import br.com.sankhya.jape.vo.DynamicVO;
    import br.com.sankhya.modelcore.dataunit.annotations.DataUnitCrudListener;
    import br.com.sankhya.modelcore.dataunit.listener.DataUnitCrudListenerContext;
    import br.com.sankhya.modelcore.dataunit.listener.IDataUnitCrudListener;
    import br.com.sankhya.modelcore.comercial.ItemNotaCrudListener;

    @DataUnitCrudListener(entity = "ItemNota", resourceId = "br.com.sankhya.mgecom.mov.selecaodedocumento")
    public class ItemNotaSelecaoPortalDataUnitCrudListener implements IDataUnitCrudListener {

        private static final Logger LOGGER = Logger.getLogger(ItemNotaSelecaoPortalDataUnitCrudListener.class.getName());

        private ItemNotaCrudListener itemNotaCrudListener;

        public ItemNotaSelecaoPortalDataUnitCrudListener() {
            this.itemNotaCrudListener = new ItemNotaCrudListener();
        }

        @Override
        public void beforeFind(DataUnitCrudListenerContext ctx) throws Exception {
            FinderWrapper finder = ctx.getFinder();
            itemNotaCrudListener.beforeFind(finder);
        }

        @Override
        public void afterLoadVOs(Collection result) throws Exception {
            itemNotaCrudListener.afterResult(result);
            result.forEach(vo -> beforeLoadRecord((DynamicVO) vo));
        }

        private void beforeLoadRecord(DynamicVO vo) {
            try {
                itemNotaCrudListener.beforeLoadRecord(vo);
            } catch (Exception e) {
                LOGGER.log(Level.SEVERE, "Error loading record: " + vo, e);
            }
        }
    }
```

**dataset.metadataInterceptor / IDataUnitInterceptor**

```
    // HTML5:
    <sk-dataset entity-name="NotaCancelada" sk-dataset-created="ctrl.onDatasetCreated(dataset)" metadata-interceptor="ctrl.metadataInterceptor">
        <sk-field pattern="NOMEFANTASIA" path="Empresa"></sk-field>
    </sk-dataset>

    function metadataInterceptor(fields, dataSet){
        fields.forEach(field => {
            if(field.id == "CODTIPOPER"){
                field.visibleAttribute = "N";
            }

            if(field.name =="Empresa.NOMEFANTASIA"){
                field.description = "label teste";
            }
        });

        return fields;
    }

    //--------------------------------------------------------------------------------------------------------------------------------

    // DS:
    // Criar uma classe com o final "DataUnitInterceptor", dentro da pasta
    // {projeto-bff}/src/br/com/sankhya/mgecom/dataUnit/interceptors/
    // implementando a "IDataUnitInterceptor", (passando a entidade e o resourceId
    // utilizados no DataUnit), sobrescrevendo os métodos que forem necessários:
    package br.com.sankhya.mgecom.dataUnit.interceptors;

    import java.util.ArrayList;
    import java.util.List;
    import br.com.sankhya.modelcore.dataunit.DataUnitFieldMap;
    import br.com.sankhya.modelcore.dataunit.annotations.DataUnitInterceptor;
    import br.com.sankhya.modelcore.dataunit.interceptor.IDataUnitInterceptor;

    @DataUnitInterceptor(entity = "NotaCancelada", resourceId = "br.com.sankhya.mgecom.mov.selecaodedocumento")
    public class NotaCanceladaSelecaoPortalDataUnitInterceptor implements IDataUnitInterceptor {

        @Override
        public void interceptFieldMetadata(DataUnitField duField) {
            if("CODTIPOPER".equals(duField.getName())) {
                duField.setVisible(false);
            }

            if("Empresa.NOMEFANTASIA".equals(duField.getName())) {
			    duField.setLabel("label teste");
		    }
        }
    }
```
