---
id: "https://developer.sankhya.com.br/docs/️-adaptadores-de-tipos"
titulo: "🗺️ Adaptadores de Tipos"
url: "https://developer.sankhya.com.br/docs/️-adaptadores-de-tipos"
atualizado_em: "2026-09-08T19:13:33.000Z"
---

# 🗺️ Adaptadores de Tipos

***

# 🗺️ Adaptadores de Tipos

## Visão Geral

Em alguns cenários, o desenvolvedor pode precisar manipular tipos de dados que não possuem suporte nativo no **SDK Sankhya** ou na biblioteca **Gson** (responsável pela serialização e deserialização de JSON).

Para resolver isso, é possível criar **Adaptadores de Tipo** — componentes responsáveis por converter valores entre:

* Formatos JSON
* Objetos Java
* Valores compatíveis com o Jape (camada de persistência)

***

<br />

## Adaptadores Globais

Adaptadores globais são aplicados automaticamente pelo SDK durante a manipulação de dados. Para criar um adaptador global, basta anotar uma classe com:

```java
@br.com.sankhya.studio.stereotypes.GlobalTypeAdapter
```

### Interfaces Disponíveis

A classe anotada pode implementar uma ou mais das interfaces abaixo:

| Interface             | Finalidade                                                      |
| --------------------- | --------------------------------------------------------------- |
| `TypeAdapter<T>`      | Converte o tipo para e a partir de valores compatíveis com Jape |
| `JsonSerializer<T>`   | Define como o tipo é convertido **para JSON**                   |
| `JsonDeserializer<T>` | Define como o tipo é convertido **a partir de JSON**            |

***

## Exemplo: Adaptador para `ZonedDateTime`

O tipo `java.time.ZonedDateTime` não possui suporte nativo pelo Gson, sendo necessário um adaptador para manipulá-lo.

O exemplo abaixo realiza:

* Conversão **VO ↔ Jape** (`fromVO` / `toVO`)
* **Serialização JSON**
* **Deserialização JSON**

```java
@GlobalTypeAdapter
public class ZonedDateTimeAdapter implements JsonSerializer<ZonedDateTime>, TypeAdapter<ZonedDateTime>, JsonDeserializer<ZonedDateTime> {

    private static final DateTimeFormatter FORMATTER = DateTimeFormatter.ISO_OFFSET_DATE_TIME;

    @Override // O tipo Jape é java.util.Timestamp
    public ZonedDateTime fromVO(Object o) {
        if (o == null) {
            return null;
        }

        Timestamp ts = (Timestamp) o;
        return ts.toInstant().atZone(ZoneId.systemDefault());
    }

    @Override // O tipo Jape é java.util.Timestamp
    public Object toVO(ZonedDateTime zonedDateTime) {
        if (zonedDateTime == null) {
            return null;
        }

        return Timestamp.from(zonedDateTime.toInstant());
    }

    @Override
    public void setType(Class<? extends ZonedDateTime> aClass) {}

    @Override
    public ZonedDateTime deserialize(JsonElement jsonElement, Type type, JsonDeserializationContext context) throws JsonParseException {
        try {
            return ZonedDateTime.parse(jsonElement.getAsString(), FORMATTER);
        } catch (Exception e) {
            throw new JsonParseException("Erro ao desserializar ZonedDateTime: " + jsonElement, e);
        }
    }

    @Override
    public JsonElement serialize(ZonedDateTime zonedDateTime, Type type, JsonSerializationContext context) {
        return new JsonPrimitive(FORMATTER.format(zonedDateTime));
    }
}
```

***

<br />

## Adaptadores Nativos

Abaixo estão os adaptadores de tipo nativos disponibilizados pelo SDK Sankhya. Eles são aplicados automaticamente quando não há um adapter customizado registrado para o tipo alvo.

| Adapter            | Tipo Java (campo na entidade)                              | Tipo VO/Jape (no banco)                                                         | Observações                                                                                                                    |
| ------------------ | ---------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| BooleanAdapter     | Boolean                                                    | String ("S"/"N") na escrita; leitura também aceita Character ('S'/'N') e String | Converte valores booleanos para "S"/"N". Na leitura, interpreta 'S' ou "S" como true.                                          |
| ByteArrayAdapter   | byte\[]                                                    | Blob, InputStream, byte\[]                                                      | Suporta conversões entre BLOB/InputStream e byte\[].                                                                           |
| CharArrayAdapter   | char\[]                                                    | String, Clob                                                                    | Converte String/Clob para char\[]; ao salvar, mantém char\[].                                                                  |
| DateAdapter        | java.time.Temporal (LocalDate, LocalTime, LocalDateTime)   | java.sql.Timestamp                                                              | O tipo exato retornado na leitura depende do tipo configurado via setType (LocalDate/LocalTime/LocalDateTime).                 |
| DurationAdapter    | java.time.Duration                                         | String ISO-8601 (ex.: PT2H30M) ou segundos (Number/String)                      | toVO retorna string ISO. fromVO aceita ISO ou total de segundos.                                                               |
| EnumAdapter        | `Enum<?>`                                                  | String/Number (conforme getValue())                                             | Na leitura, tenta casar obj com enum.getValue(); na ausência, usa name(). Na escrita, usa getValue() se existir, senão name(). |
| HashValueAdapter   | HashValue                                                  | String no formato "ALGORITHM:hex"                                               | Ex.: "SHA-256:a665...". Se algoritmo não for informado, assume "SHA-256".                                                      |
| InputStreamAdapter | java.io.InputStream                                        | Blob, byte\[]                                                                   | Converte Blob/byte\[] para InputStream; ao salvar, transforma InputStream em byte\[].                                          |
| InstantAdapter     | java.time.Instant                                          | String ISO-8601 ou epoch millis (Number/String)                                 | toVO retorna string ISO; fromVO aceita ISO ou epoch millis.                                                                    |
| JsonElementAdapter | com.google.gson.JsonElement                                | String JSON                                                                     | Strings vazias viram JsonObject vazio; valores inválidos lançam IllegalArgumentException.                                      |
| JsonObjectAdapter  | com.google.gson.JsonObject                                 | String JSON (objeto)                                                            | Exige JSON de objeto; se não for objeto, lança IllegalArgumentException.                                                       |
| NumberAdapter      | Number (int, long, double, float, short, byte, BigDecimal) | BigDecimal                                                                      | Converte BigDecimal do banco para o tipo numérico do campo e vice-versa.                                                       |
| PeriodAdapter      | java.time.Period                                           | String ISO-8601 (P...) ou formato custom "1Y-2M-15D"                            | toVO retorna ISO; fromVO aceita ISO e formato custom.                                                                          |
| URLAdapter         | java.net.URL                                               | String                                                                          | Valida e converte URLs; possui utilitários para normalização.                                                                  |
| UUIDAdapter        | java.util.UUID                                             | String (canônico) ou byte\[16]                                                  | toVO retorna string canônica; fromVO aceita string e array de 16 bytes.                                                        |

> Observação: A resolução de adapters segue a ordem de precedência: global → nativos.<br />Isso signfica que um adaptador Global pode Sobrescrever um nativo.

## Conclusão

Adaptadores globais permitem estender o suporte nativo de tipos no SDK Sankhya, garantindo compatibilidade e consistência entre a camada de dados, JSON e objetos Java.

Caso tenha dúvidas, participe da comunidade desenvolvedora no portal ou entre em contato pelo e-mail informado no início desta página.
