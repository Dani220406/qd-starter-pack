from pytest_mock import MockerFixture
import calculator

def test_calculator(mocker: MockerFixture) -> None:
    #Arrange
    mock_a = 10
    mock_b = 5.0
    spy_somma = mocker.spy(calculator, "somma")
    spy_differenza = mocker.spy(calculator, "differenza")
    spy_prodotto = mocker.spy(calculator, "prodotto")
    spy_divisione = mocker.spy(calculator, "divisione")

    #Act
    res_somma = calculator.somma(mock_a, mock_b)
    res_differenza = calculator.differenza(mock_a, mock_b)
    res_prodotto = calculator.prodotto(mock_a, mock_b)
    res_divisione = calculator.divisione(mock_a, mock_b)

    #Assert
    assert type(res_somma) is int or float
    assert res_somma == 15
    assert spy_somma.call_count == 1
    spy_somma.assert_called_with(mock_a,mock_b)

    assert type(res_differenza) is int or float
    assert res_differenza == 5
    assert spy_differenza.call_count == 1
    spy_differenza.assert_called_with(mock_a,mock_b)

    assert type(res_prodotto) is int or float
    assert res_prodotto == 50
    assert spy_prodotto.call_count == 1
    spy_prodotto.assert_called_with(mock_a,mock_b)

    assert type(res_divisione) is int or float
    assert res_divisione == 2.0
    assert spy_divisione.call_count == 1
    spy_divisione.assert_called_with(mock_a,mock_b)