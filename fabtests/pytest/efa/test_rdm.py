import pytest

from default.test_rdm import test_rdm
from default.test_rdm import test_rdm_bw_functional

@pytest.mark.parametrize("iteration_type",
                         [pytest.param("short", marks=pytest.mark.short),
                          pytest.param("standard", marks=pytest.mark.standard)])
def test_rdm_pingpong(cmdline_args, iteration_type, completion_type, memory_type):
    from efa.efa_common import efa_run_client_server_test
    efa_run_client_server_test(cmdline_args, "fi_rdm_pingpong", iteration_type,
                               completion_type, memory_type, "all")

@pytest.mark.functional
def test_rdm_pingpong_range(cmdline_args, completion_type, memory_type, message_size):
    from efa.efa_common import efa_run_client_server_test
    efa_run_client_server_test(cmdline_args, "fi_rdm_pingpong", "short",
                               completion_type, memory_type, message_size)

@pytest.mark.parametrize("iteration_type",
                         [pytest.param("short", marks=pytest.mark.short),
                          pytest.param("standard", marks=pytest.mark.standard)])
def test_rdm_tagged_pingpong(cmdline_args, iteration_type, completion_type, memory_type):
    from efa.efa_common import efa_run_client_server_test
    efa_run_client_server_test(cmdline_args, "fi_rdm_tagged_pingpong", iteration_type,
                               completion_type, memory_type, "all")

@pytest.mark.functional
def test_rdm_tagged_pingpong_range(cmdline_args, completion_type, memory_type, message_size):
    from efa.efa_common import efa_run_client_server_test
    efa_run_client_server_test(cmdline_args, "fi_rdm_tagged_pingpong", "short",
                               completion_type, memory_type, message_size)

@pytest.mark.parametrize("iteration_type",
                         [pytest.param("short", marks=pytest.mark.short),
                          pytest.param("standard", marks=pytest.mark.standard)])
def test_rdm_tagged_bw(cmdline_args, iteration_type, completion_type, memory_type):
    from efa.efa_common import efa_run_client_server_test
    efa_run_client_server_test(cmdline_args, "fi_rdm_tagged_bw", iteration_type,
                               completion_type, memory_type, "all")

@pytest.mark.functional
def test_rdm_tagged_bw_range(cmdline_args, completion_type, memory_type, message_size):
    from efa.efa_common import efa_run_client_server_test
    efa_run_client_server_test(cmdline_args, "fi_rdm_tagged_bw", "short",
                               completion_type, memory_type, message_size)

@pytest.mark.parametrize("iteration_type",
                         [pytest.param("short", marks=pytest.mark.short),
                          pytest.param("standard", marks=pytest.mark.standard)])
def test_rdm_atomic(cmdline_args, iteration_type, completion_type, memory_type):
    from common import ClientServerTest
    # the rdm_atomic test's run time has a high variance when running single c6gn instance.
    # the issue is tracked in:  https://github.com/ofiwg/libfabric/issues/7002
    # to mitigate the issue, set the maximum timeout of fi_rdm_atomic to 1800 seconds.

    test = ClientServerTest(cmdline_args, "fi_rdm_atomic", iteration_type, completion_type,
                            memory_type=memory_type, timeout=1800)
    test.run()

