#!/usr/bin/python3
# Function for calculating hours worked
import sys;

def CalculeteOvertime(qtde_extra_hour, hourValue):
  return (hourValue * 1.5)  * qtde_extra_hour ;

def CalculateHours(amountHours, hourValue):  
  amountHours =float(amountHours);
  hourValue =float(hourValue);

  if amountHours > 40:   
    qtde_extra_hour = amountHours - 40;
    print("Quantidade de hora extra: ", str(qtde_extra_hour))
    overtimeValue = CalculeteOvertime(qtde_extra_hour, hourValue);
    print("Valor hora extra: ", str(overtimeValue))

    wage = 40 * hourValue + overtimeValue;
  else:
    wage = amountHours * hourValue;

  return wage;

if len(sys.argv) < 3:
  print("Quantidade de paramêtros incorreto\n");
  print("Exemplo: python3 challenge01_parameters 40 35.0");
  exit(0);
else:
  amountHours = sys.argv[1];
  hourValue = sys.argv[2];

payment = CalculateHours(amountHours, hourValue);
print("Salário semanal: ", str(payment));
