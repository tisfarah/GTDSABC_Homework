Sub EasyChallenge()

' Create variables for the code
Dim ws As Worksheet
Dim Ticker As String

                       
'This is the start of the loop that will run through each worksheet
For Each ws In Worksheets


'The following searches through the ticker column to spit out a list of the unique ticker values
ActiveSheet.Range("A:A").AdvancedFilter Action:=xlFilterCopy, CopyToRange:=ActiveSheet.Range("i1"), Unique:=True

'Create headers for the Ticker symbol and its corresponding total volume
    Range("i1").Value = "Ticker"
    Range("J1").Value = "Total Volume"

    Dim VolumeTotal As Double
    VolumeTotal = 0 ' Initialize VolumeTotal to start at 0
    Dim i, j As Integer

    ' Use last row formula to determine the last row and end point for loop
    LastRowTicker = Cells(Rows.Count, 9).End(xlUp).Row

    For Tick = 2 To LastRowTicker
    
        TickerVolume = Cells(Tick, 9).Value
        ActiveSheet.Cells(Tick, 10) = Application.SumIf(Range("A:A"), TickerVolume, Range("G:G"))
    
    Next Tick
                    
        
Next ws

End Sub
