---
id: "42427596791831"
titulo: "Como criar um campo de valor por extenso"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427596791831-Como-criar-um-campo-de-valor-por-extenso"
trilha: "PLOOMES: Automação de propostas  > Campos e formulários"
atualizado_em: "2026-08-10T18:05:43Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452343", "sync_hash_8cd664a74fef"]
---

# Como criar um campo de valor por extenso

Disponibilizamos uma fórmula em JavaScript que permite transformar valores numéricos em suas representações por extenso, sem necessidade de desenvolver uma API externa ou saber programar.

---

## Como configurar

Nesse exemplo criarei um campo no formulário de negócios, mas o mesmo pode ser feito em clientes, propostas, vendas, documentos ou produtos (qualquer campo com fórmulas).

Veja agora o passo a passo de como realizar essa configuração:

### 1. Crie um campo de texto simples;

### 2. Edite a fórmula em "Configurações avançadas":

![Print da tela de criação/edição de campo destacando o tipo de](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329071/7b4925646681dd8a01169efc/mceclip0.png?expires=1786536000&signature=c5f9e3663629e41e8deabb3f856a58cff09148c7230740588a421164e2d1a12a&req=dyYuFct3nYZeFb4V1XW4gckLfLi7quTFCzFFxF7ltzFne6%2B63H%2Fh%2Bt4g2QeF%0AKFCPEBbm7Dxm1PQju5u1vVkv%2Bg%3D%3D%0A)

### 3. Selecione o tipo "Fórmula simples":

![Imagem 2: 3. Selecione o tipo "Fórmula simples":](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1793082703/59b322dc72cca0d133e39f73d9dd/image.png?expires=1786536000&signature=714d1781f7a3b6963899b2602ff67b99ac0c949a3c6b95de247e65275354fe0c&req=dScuFcl2n4ZfWvMW3nq%2BgSd%2BgVqn7NW%2B9eZSiHUi9VAfJ2xfZIq2MZHj1Gc%2F%0ArRBmGlZ6XRR4A%2BAD19fvPk3xFVo%3D%0A)

### 4. Na fórmula, insira este código :

```
(function (valor, monetario) {
    if(parseFloat(valor) == 0){
        return "Zero"
    }

    const unidades = Array.of("", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove");
    const dezenas = Array.of("", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa");
    const especiais = Array.of("dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove");
    const centenas = Array.of("", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos");

    const escalas = Array.of(
        "",
        "mil",
        Array.of("milhão", "milhões"),
        Array.of("bilhão", "bilhões"),
        Array.of("trilhão", "trilhões"),
        Array.of("quadrilhão", "quadrilhões"),
        Array.of("quintilhão", "quintilhões"),
        Array.of("sextilhão", "sextilhões"),
        Array.of("setilhão", "setilhões"),
        Array.of("octilhão", "octilhões"),
        Array.of("nonilhão","nonilhões")
    );

    function triplaParaTexto(n) {
        n = parseInt(n, 10);
        if (n === 0) return "";

        let c = Math.floor(n / 100);
        let d = Math.floor((n % 100) / 10);
        let u = n % 10;
        let texto = "";

        if (n === 100) return "cem";

        if (c > 0) texto += centenas.at(c);
        if (d === 1) {
            texto += (texto ? " e " : "") + especiais.at(u);
        } else {
            if (d > 0) texto += (texto ? " e " : "") + dezenas.at(d);
            if (u > 0) texto += (texto ? " e " : "") + unidades.at(u);
        }

        return texto;
    }

    function inteiroParaExtenso(n) {
        if (n === 0) return "zero";

        let partes = new Array();
        let blocos = new Array();

        // Quebrar número em blocos de 3 dígitos da direita para a esquerda
        while (n > 0) {
            blocos.push(n % 1000);
            n = Math.floor(n / 1000);
        }

        for (let i = blocos.length - 1; i >= 0; i--) {
            let bloco = blocos.at(i);
            if (bloco === 0) continue;

            let texto = triplaParaTexto(bloco);

            let escala = escalas.at(i);
            if (i === 0) {
                partes.push(texto);
            } else if (i === 1) {
                partes.push(texto + " mil");
            } else {
                let nome = bloco === 1 ? escala.at(0) : escala.at(1);
                partes.push(texto + " " + nome);
            }
        }

        // Juntar com "e" se necessário
        let final = partes.join(" ");
        return final;
    }

    function centavosParaExtenso(n) {
        if (n === 0) return "";
        return inteiroParaExtenso(n) + (n === 1 ? " centavo" : " centavos");
    }

    valor = parseFloat(valor).toFixed(2);
    let partes = valor.split('.').map(Number);
    let inteiro = partes.at(0);
    let centavos = partes.at(1);

    let extenso = "";

    if(monetario){
            if (inteiro > 0) {
            extenso += inteiroParaExtenso(inteiro) + (inteiro === 1 ? " real" : " reais");
        }

        if (centavos > 0) {
            if (extenso) extenso += " e ";
            extenso += centavosParaExtenso(centavos);
        }
    } else {
        extenso += inteiroParaExtenso(inteiro)
    }

    return extenso.charAt(0).toUpperCase() + extenso.slice(1);
})([CAMPO], true)
```

### 5. Substitua "[CAMPO]", no final da fórmula, pelo campo que possui o valor a ser escrito por extenso.

Você pode selecionar um campo assim:

[GIF animado: Imagem 3: Você pode selecionar um campo assim:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1793611873/7ba9ac01904862b18c268ec16cbb/Anima%C3%A7%C3%A3oID29075864443534s556456.gif?expires=1786536000&signature=48a43b8248bffd29de6ba75a47fc3c2666e4b4996487035e799b7dffd956c498&req=dScuFc9%2FnIlYWvMW3nq%2BgZFMEh2U7Cvrso4SMOho2mnXzGi4E4OzEZK57zV0%0Ag2tLZ5yacByAgbDkw8sFP1lSSoA%3D%0A)

## Resultado

Na configuração:

![Imagem 4: Na configuração:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1793612699/9531da86a8b32af99ee60ea8682d/image.png?expires=1786536000&signature=2a74751a9e3062f6fec5adaaa9900eebb8da08f5dfd582dd427b8a76d1726130&req=dScuFc9%2Fn4dWUPMW3nq%2BgbsLe1VW%2FZLXIfDHgStPu%2B1tx4pVW6id1jGMDuBb%0AHg%2FTNOOo1khhuhmmfX0ep9yTLH0%3D%0A)

No formulário:

![Imagem 5: No formulário:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1793195471/e79c7eccb3e0b6bec8d5b7bc12e4/image.png?expires=1786536000&signature=5959e363efd4299f71fc2efe0cd038cea2cb53ca921b90c1cc06e22786c20713&req=dScuFch3mIVYWPMW3nq%2BgU22v7SaUvOsLFTQ2FxNIwvXw7TZebPgiOxX3V7e%0AwOiSP54kFTk4Pdn5Zq57y0DjHMI%3D%0A)

---

**Caso necessite de informações adicionais ou suporte, estamos à disposição para ajudar!**
