@extends('layout')

@section('content')
    <link rel="stylesheet" href="{{asset('/css/home.css')}}">

    <div class="jumbotron">
        <div class="container">
            <h1>标题</h1>
        </div>
    </div>

    <div class="col-md-12 container-fluid">
        <div class="row">
            @foreach ($items as $item)
                <div class="col-xs-12 col-sm-4 col-md-3">
                    <div class="thumbnail" style="height: 320px">
                        <div  class="pic">
                            <a href="{{ $item->url }}" target="_blank">
                                <img src="http://{{env('PIC_HOST')}}/{{ $item->pic_url }}">
                            </a>
                        </div>
                        <div class="caption">
                            <h2 class="itemName">
                                <a href="{{ $item->url }}" target="_blank">
                                    <span class="black">{{ $item->title }}</span>
                                    <span class="red">{{ $item->price }}</span>
                                </a>
                            </h2>
                            <div class="timeInfo">
                                <span class="time">{{ date('m-d H:i', $item->timestamp) }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            @endforeach
        </div>

        <nav>
            <?php echo $items->render(); ?>
        </nav>
    </div>
@endsection