---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-form-config/"
titulo: "Simple Form Config"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-form-config/"
trilha: "Docs > Components > Sankhya Erp Componentes > Snk Simple Form Config"
---

# Simple Form Config

O **[SnkSimpleFormConfig](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-form-config)** é um componente
que realiz a configuração de um formulário simplificado, geralmente utilizado no [SnkSimpleCrud](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-crud)

[![Imagem 1: O SnkSimpleFormConfig é um componente que realiz a configuração de um formulário simplificado, geralmente utilizado no…](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-simple-form-config/demo-simple-form-config.png)](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/snk-simple-form-config/demo-simple-form-config.png)

```
import React from 'react';
import { SnkApplication, SnkSimpleFormConfig } from "@sankhyalabs/sankhyablocks/react/components";

const Demo = () => {
    const paymentMethodsRef = useRef(null);
    const [paymentMethodsDataUnit, setPaymentMethodsDataUnit] = useState(null);

    useEffect(() => {
        setPaymentMethodsDataUnit(new DataUnit("paymentMethods"));
    }, []);

    return (
        <SnkApplication configName="Payments">
            <SnkSimpleFormConfig ref={paymentMethodsRef} dataUnit={paymentMethodsDataUnit} configName={'PaymentsFormConfig'} />
        </SnkApplication>
    );
}

export default Demo;
```

## Chave da configuração do formulário

> Propriedade utilizada: **configName**

É preciso informar a chave das configurações do formulário, salva no banco de dados.
Exemplo:
`FormCfg:GradeItensFormConfig-PA:br.com.sankhya.com.mov.CentralNotas:TIPMOV-P-8`

## Unidade de dados responsável

> Propriedade utilizada: **dataUnit**

O **[SnkSimpleFormConfig](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/sankhya-erp-componentes/snk-simple-form-config)** precisa receber
o dataUnit relativo ao formulário que receberá as alterações.

## Métodos

### show

Responsável por exibir o componente na tela.
