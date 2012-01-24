from nagioscheck import NagiosCheck, Status
from StringIO import StringIO

class WouldHaveExitNonZero(Exception):
    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return "%s(%d)" % (self.__class__.__name__, self.code)

class OptimisticCheck(NagiosCheck):
    version = '1.2.3'

    expect = "SUNSHINE LOLLIPOPS"

    def __init__(self, *args, **kwargs):
        NagiosCheck.__init__(self, *args, **kwargs)

        self.add_option('f', 'foo', 'foo', "Foo foo?")

    def check(self, opts, args):
        raise Status('ok', self.expect)

class PessimisticCheck(NagiosCheck):
    version = '1.2.3'

    expect = "YOU DUN MADE ME MAD"

    def __init__(self, *args, **kwargs):
        NagiosCheck.__init__(self, *args, **kwargs)

        self.add_option('b', 'bar', 'bar', "Bar bar?")

    def check(self, opts, args):
        raise Status('critical', self.expect)

def raise_exception_on_exit(code):
    """Raise an exception instead of exiting fo' real."""
    if code == 0:
    	pass # No big deal
    else:
    	raise WouldHaveExitNonZero(code)

def test_for_ok_from_cli():
    outio = StringIO()
    errio = StringIO()
    OptimisticCheck(outio, errio, raise_exception_on_exit).run()
    out = outio.getvalue()
    assert out.startswith("OK:")
    assert out.find(OptimisticCheck.expect) != -1
    errio.close()
    outio.close()

def test_for_critical_from_cli():
    outio = StringIO()
    errio = StringIO()
    try:
        PessimisticCheck(outio, errio, raise_exception_on_exit).run()
    except WouldHaveExitNonZero, e:
        assert e.code == Status.EXIT_CRITICAL
    out = outio.getvalue()
    assert out.startswith("CRITICAL:")
    assert out.find(PessimisticCheck.expect) != -1
    errio.close()
    outio.close()
