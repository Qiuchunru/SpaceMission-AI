
from backend.ai import analyze_mission, analyze_telemetry



def test_analyze_mission():

    result = analyze_mission(

        "Europa Exploration Mission",

        "Search for possible water resources",

        "Limited energy and communication delay"

    )


    assert result is not None

    assert "Mission Analysis" in result

    assert "Risk Assessment" in result





def test_analyze_telemetry():

    result = analyze_telemetry(

        """
        Temperature: 85C
        Battery: 30%
        Signal: Weak
        """

    )


    assert result is not None

    assert "Telemetry Analysis" in result
